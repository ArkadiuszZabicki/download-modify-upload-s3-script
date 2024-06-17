import boto3
import os

def s3_client():
    s3 = boto3.client('s3')
    return s3

def s3_resource():
    s3 = boto3.resource('s3')
    return s3

def download_file_from_bucket(bucket_name, object_key):
    bucket_name = bucket_name
    object_key = object_key
    file_path = os.path.dirname(__file__) + '/' + object_key
    s3_resource().meta.client.download_file(bucket_name, object_key, file_path)

def upload_file_to_bucket(bucket_name, object_key):
    file_path = os.path.dirname(__file__) + '/' + object_key
    s3_client().upload_file(file_path, bucket_name, object_key)

