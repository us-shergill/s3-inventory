#!/bin/bash
source_bucket=$1


## Set up s3 bucket inventory
JSON_STRING=$( jq -n \
                  --arg destination_bucket "$2" \
                  --arg account_id "$3" \
                  '{Destination: { S3BucketDestination: { AccountId: $account_id, Bucket: $destination_bucket, Format: "CSV" }}, IsEnabled: true, Id: "2", IncludedObjectVersions: "Current", Schedule: { Frequency: "Daily" }}' )
echo "$JSON_STRING"
aws s3api put-bucket-inventory-configuration --bucket $source_bucket --id 2 --inventory-configuration "$JSON_STRING"
aws s3api put-bucket-policy --bucket "$4" --policy file://policy.json