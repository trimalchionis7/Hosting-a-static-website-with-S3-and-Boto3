# Hosting a static website using S3

import boto3

# Create S3 client
s3 = boto3.client('s3')

# Assign policy to selected bucket
s3.put_bucket_website(
    Bucket='jonnie-static-website',
    WebsiteConfiguration={
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
})