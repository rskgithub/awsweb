import boto3
import os


def upload_to_s3(file, bucket_name, acl="public-read"):
    """
    Funtion is used for connecting to the AWS instance
    and upload a file to the bucket. The access keys and access secret keys
    are stored in the environment variables
    :param file: File object
    :return:
    """
    client = boto3.client(
        's3',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],

    )
    try:

        client.upload_fileobj(
            file,
            bucket_name,
            file.name,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e
