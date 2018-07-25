# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:2.7.9

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /book_api

# Set the working directory to /music_service
WORKDIR /book_api

# Copy the current directory contents into the container at /music_service
ADD . /book_api/

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000:8000
