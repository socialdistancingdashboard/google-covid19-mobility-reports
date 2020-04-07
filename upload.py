import json
from datetime import datetime, timedelta
import boto3
from datetime import datetime, timedelta

s3 = boto3.resource('s3')
date_str = name.split('+')[0]
date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
print(date.strftime("%Y-%m-%d"))
s3.meta.client.upload_file('data/processed/mobility_reports.csv', "sdd-s3-bucket", 'mobility_reports/{}/{}/{}.csv'.format(str(date.year).zfill(4), str(date.month).zfill(2), str(date.day).zfill(2)))
