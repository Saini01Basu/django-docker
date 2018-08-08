node {
  stage 'Checkout'
    git 'https://github.com/Saini01Basu/django-docker.git'
  
  stage 'Cloudformation'
    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'default_cred', variable: 'AWS_ACCESS_KEY_ID']]) {
      sh "aws configure set aws_access_key_id ${env.AWS_ACCESS_KEY_ID}"
      sh "aws configure set aws_secret_access_key ${env.AWS_SECRET_ACCESS_KEY}"
      sh "aws configure set default.region us-east-1"
    }
    def command = "aws cloudformation update-stack --template-body file://template.json --stack-name moveStack --parameter ParameterKey=DesiredCapacity,ParameterValue=1, ParameterKey=VpcId,ParameterValue=vpc-007fc05093485e7e6, ParameterKey=InstanceType,ParameterValue=t2.micro ParameterKey=KeyName,ParameterValue=saini ParameterKey=MaxSize,ParameterValue=1"
    try {
      def proc = ["/bin/sh", "-c", command].execute()
      proc.waitFor()
      echo "The exit value is : ${proc.exitValue()}"
      script {
        if (proc.exitValue() != 0) {
          echo "stack is already updated"
          
        }
      }
    }
    catch (Exception e) {
    }
  
  stage 'Docker build'
    docker.build('move-repo')
 
  stage 'Docker push'
    docker.withRegistry('https://088072595747.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:default_cred') {
        docker.image('move-repo').push('latest')
    }

  stage 'Run Service'
    sh "aws ecs run-task --cluster new-stack-ECSCluster-10FGUKOHUY5BH --task-definition new-stackmove-ecs --count 1 --launch-type EC2"
}
