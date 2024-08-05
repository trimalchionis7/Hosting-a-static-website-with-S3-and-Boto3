# Hosting a static website using Amazon S3 and Boto3

[Work in progress]

Some basic Python scripts to host a website using S3 and the Amazon SDK Boto 3, which perform the following functions:
- create a S3 bucket ('s3-bucket-creation.py')
- grant the bucket public read & write permissions ('s3-bucket-policy.py')
- upload 2 HTML files ('index.html', 'error.html') to the S3 bucket
- configure the bucket to host the index file as static webpage ('s3-website-hosting.py').
