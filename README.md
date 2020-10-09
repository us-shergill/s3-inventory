### Steps to run
On a MacOS
I use the s3 inventory to generate the s3 metadata .
Amazon S3 inventory is one of the tools Amazon S3 provides to help manage your storage.
https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html
```
$ brew install jq
```
###Execute Script
source_bucket - the bucket to scan for files
destination_bucket - bucket where inventory for source bucket is saved
```
$  bash ./create_s3_inventory.sh "source_bucket" "destination_bucket_arn" "account_id" "destination_bucket"
```
execute python script . change the bucket names 
```
$ python s3_inventory_parser.py
```