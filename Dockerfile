# Use the official Python 3.9 slim-buster image as the base image
FROM python:3.9-slim-buster

# Copy the contents of the current directory into the /app directory in the container
COPY . /app  

# Set the working directory within the container to /app
WORKDIR /app  # Set the working directory within the container to /app

# Update package repository and install the AWS CLI tool
RUN apt update -y && apt install awscli -y

# Update package repository again and install Python dependencies from requirements.txt
RUN apt-get update && pip install -r requirements.txt

# Define the command to run when the container starts
CMD ["python", "app.py"]