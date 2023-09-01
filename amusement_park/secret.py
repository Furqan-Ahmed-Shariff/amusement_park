import boto3
from botocore.exceptions import ClientError
import json


def get_secret():
    secret_name = "rds!db-d7f68eb5-4768-4451-a90b-c3735e3b8d6d"
    region_name = "ap-south-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response["SecretString"]

    # Your code goes here.
    secret = json.loads(secret)
    return secret["password"]
