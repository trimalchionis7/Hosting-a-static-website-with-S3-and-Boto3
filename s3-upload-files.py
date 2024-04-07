# Upload the files to the S3 bucket

import boto3

s3 = boto3.client('s3')

filename = ['index.html', 'error.html']
bucket_name = 'jonnie-static-website'



for file in filename:
    data = open(file, 'rb')
    s3.put_object(Body=data, 
                  Bucket='jonnie-static-website', 
                  Key=file, 
                  ContentType='text/html')