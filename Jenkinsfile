node {
  stage 'Checkout'
    git 'https://github.com/Saini01Basu/django-docker.git'
  
  stage 'Cloudformation'
    sh "aws configure set default.region us-east-1"
    sh "aws cloudformation deploy --template-file template.json --stack-name moveStack --parameter-overrides DesiredCapacity=1 InstanceType=t2.micro KeyName=saini MaxSize=1 SubnetId=subnet-0c995c77750f1a898,subnet-0156d2677c8e96a27 VpcId=vpc-007fc05093485e7e6"
 
  stage 'Docker build'
    docker.withRegistry('https://088072595747.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:ecr-credentials') {
        docker.build('move-repo')
    }
 
  stage 'Docker push'
    docker.withRegistry('https://088072595747.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:ecr-credentials') {
        docker.image('move-repo').push('latest')
    }

  stage 'Run Service'
    sh "aws ecs create-service --service-name move-service --task-definition moveStackmove-ecs --desired-count 1"
}
