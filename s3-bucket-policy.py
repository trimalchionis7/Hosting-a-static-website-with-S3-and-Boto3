# Assign bucket policy

import boto3
import json

s3 = boto3.client('s3')
bucket_name = 'jonnie-static-website'

# Disable public access settings & set ACL
s3.put_public_access_block(
    Bucket=bucket_name,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    })

s3.put_bucket_acl(Bucket=bucket_name, ACL='public-read-write')

bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': "arn:aws:s3:::%s/*" % bucket_name
    }]
}

bucket_policy = json.dumps(bucket_policy)
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)