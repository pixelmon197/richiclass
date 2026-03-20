import boto3
import os

client= boto3.client(
        "cognito.idp",
        region_name=os.environ.get("AWS_REGION")
)

USER_POOL_ID = os.environ.get("USER_POOL_ID")


def create_cognito_user(email: str, password: str):
    response = client.admin_create_user(
        UserPoolId= USER_POOL_ID,
        Username= email,
        UserAttributes=[
            {"Name": "email", "Value": email},
            {"Name": "email_verified", "Value":True}
        ],
        MessageAction="SUPRESS"
    )

    client.admin_set_user_password()