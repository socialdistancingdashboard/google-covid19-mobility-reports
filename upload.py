import json
from datetime import datetime, timedelta
import boto3

client = boto3.client('s3')

# Upload data to S3
s3.Bucket('sdd-s3-bucket').upload_file('/data/processed/mobility_reports.csv','googlereports/'+str(date.year).zfill(4)+'/'+str(date.month).zfill(2)+'/'+str(date.day).zfill(2)')
