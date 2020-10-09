import json
import csv
import gzip
import boto3
s3 = boto3.resource('s3')


def list_keys(bucket, manifest_key):
    manifest = json.load(s3.Object(bucket, manifest_key).get()['Body'])
    for obj in manifest['files']:
        gzip_obj = s3.Object(bucket_name=bucket, key=obj['key'])
        buffer = gzip.open(gzip_obj.get()["Body"], mode='rt')
        reader = csv.reader(buffer)
        for row in reader:
            yield row


if __name__ == '__main__':
    bucket = 's3-inventory-bucket'
    manifest_key = 'path/to/my/inventory/manifest.json'

    for bucket, key, *rest in list_keys(bucket, manifest_key):
        print(bucket, key, *rest)