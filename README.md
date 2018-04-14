# AWS Services integration Using boto3 and Django
A Django Web App for Showing Boto3 and AWS integration
Technologies used:
  1. Django 1.11
  2. Python3.6
  3. Boto3
  
  
This is a tutorial showing how to use the boto3 library with a Django app to access and use the services provided by AWS.
This tutorial assumes the AWS credentials are stored in the Environment variables.
## Adding The AWS Credentials to the Environment Variables
### Linux
Edit the .bashrc file using any of your favourite editor and add the following lines:

export AWS_ACCESS_KEY_ID=access_key
export AWS_SECRET_ACCESS_KEY=access_secret_key
export AWS_DEFAULT_REGION=default_region
