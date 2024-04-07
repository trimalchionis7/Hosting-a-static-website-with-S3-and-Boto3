# Creating S3 bucket

import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='jonnie-static-website',
                 ObjectOwnership='ObjectWriter',
                 CreateBucketConfiguration={'LocationConstraint': 'eu-central-1'})