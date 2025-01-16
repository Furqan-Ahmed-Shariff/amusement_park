Django Web App Deployment on AWS Elastic Beanstalk
This repository contains the setup for deploying a Django web application to AWS Elastic Beanstalk. The deployment includes using Elastic Beanstalk CLI, configuring the environment, and using the .ebextensions folder for further customization. The app utilizes Amazon RDS for database management and AWS Route 53 for domain name configuration.

Prerequisites
Before starting, ensure you have the following tools installed on your local machine:

AWS Account: You must have an AWS account to create and manage resources on Elastic Beanstalk.
AWS CLI: Command Line Interface to interact with AWS services. Install it by running:
pip install awscli

Then configure the AWS CLI with your credentials:
aws configure

Elastic Beanstalk CLI (EB CLI): CLI tool for deploying and managing your Elastic Beanstalk application:
pip install awsebcli

Python (preferably Python 3.x)
Django: Make sure your Django project is ready and working locally.
Git: Version control to push the code to GitHub and later deploy.

This project includes a .ebextensions directory that configures various Elastic Beanstalk settings, installs necessary packages, and runs custom commands during deployment.

Key Sections in django.config:
option_settings: Specifies the WSGI path for your Django app.
packages: Installs necessary system packages

Initialize Elastic Beanstalk Application
Once the Django app is ready, it's time to initialize the Elastic Beanstalk application.

Navigate to your project folder:
cd /path/to/your/django/project

Initialize the Elastic Beanstalk application: Run the following command and follow the prompts:
eb init
Select the appropriate options for the AWS region and platform (Python).

Create the Elastic Beanstalk environment: Create the environment with:
eb create my-environment-name

Elastic Beanstalk will automatically create an EC2 instance, load balancer, and RDS if configured.

Deploy the Application
Once the environment is set up, deploy your Django application using:
eb deploy

Access Your Application
Once the deployment is complete, you can open your application in a web browser using the command:
eb open
