import boto3
import uuid

s3 = boto3.client("s3")
BUCKET_NAME = "your-whistleke-bucket"

def upload_media(file):
    ext = file.filename.split('.')[-1]
    key = f"leaks/{uuid.uuid4()}.{ext}"
    s3.upload_fileobj(file.file, BUCKET_NAME, key)
    url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{key}"
    return url
