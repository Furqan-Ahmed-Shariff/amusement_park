# Django Web App Deployment on AWS Elastic Beanstalk

This repository contains the setup for deploying a Django web application to AWS Elastic Beanstalk. The deployment includes using Elastic Beanstalk CLI, configuring the environment, and using the .ebextensions folder for further customization. The app utilizes Amazon RDS for database management and AWS Route 53 for domain name configuration.

## 1. Prerequisites
Before starting, ensure you have the following tools installed on your local machine:

### AWS Account: 
You must have an AWS account to create and manage resources on Elastic Beanstalk.

### AWS CLI: 
Command Line Interface to interact with AWS services. Install it by running:
```
pip install awscli
```

### Then configure the AWS CLI with your credentials:
```
aws configure
```

### Elastic Beanstalk CLI (EB CLI): 
CLI tool for deploying and managing your Elastic Beanstalk application:
```
pip install awsebcli
```

### Python:
preferably Python 3.x

### Django:
Make sure your Django project is ready and working locally.

### Git: 
Version control to push the code to GitHub and later deploy.

## 2. .ebextensions Directory
This project includes a .ebextensions directory that configures various Elastic Beanstalk settings, installs necessary packages, and runs custom commands during deployment.

### Key Sections in django.config:
option_settings: Specifies the WSGI path for your Django app.
packages: Installs necessary system packages

## 3. Initialize Elastic Beanstalk Application
Once the Django app is ready, it's time to initialize the Elastic Beanstalk application.

### Navigate to your project folder:
cd /path/to/your/django/project

### Initialize the Elastic Beanstalk application: Run the following command and follow the prompts:
```
eb init
```
Select the appropriate options for the AWS region and platform (Python).

### Create the Elastic Beanstalk environment: 
Create the environment with:
```
eb create my-environment-name
```
Elastic Beanstalk will automatically create an EC2 instance, load balancer, and RDS if configured.

## 4. Deploy the Application
Once the environment is set up, deploy your Django application using:
```
eb deploy
```

## 5. Access Your Application
Once the deployment is complete, you can open your application in a web browser using the command:
```
eb open
```
This will open the Elastic Beanstalk environment URL in your default browser.

This setup guide helps you deploy an illustrative Django web app on AWS Elastic Beanstalk using the EB CLI, configure the environment using .ebextensions, and deploy the application with Amazon RDS for database management. You can customize the deployment further with scaling, security, and other AWS services.

Feel free to clone this repository and modify it according to your needs. Happy coding! 
