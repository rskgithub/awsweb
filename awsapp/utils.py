import boto3
import os


def get_aws_client():
    """
    Function will connect to the AWS instance
    using the credentials stored in the environment variable
    :return: client(boto client)
    """
    return boto3.client(
        's3',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],

    )


def list_all_buckets():
    """
    Function will connect to the AWS instance and will return a list of
    all the buckets
    :return: a list of buckets
    """
    # get the s3 client
    client = get_aws_client()

    # Call S3 to list current buckets
    response = client.list_buckets()

    # Get a list of all bucket names
    buckets = [(bucket['Name'], bucket['Name']) for bucket in response['Buckets']]

    return buckets


def upload_to_s3(file, bucket_name, acl="public-read"):
    """
    Funtion is used for connecting to the AWS instance
    and upload a file to the bucket. The access keys and access secret keys
    are stored in the environment variables
    :param file: File object
    :param bucket_name: s3 bucket name
    :param acl: permissions
    :return:
    """
    client = get_aws_client()
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
