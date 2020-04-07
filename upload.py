import json
from datetime import datetime, timedelta
import boto3

client = boto3.client('s3')

s3.meta.client.upload_file('/data/processed/mobility_reports.csv', "ssd-s3-bucket", "mobility_reports.csv")


