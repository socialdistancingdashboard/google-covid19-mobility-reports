import json
from datetime import datetime, timedelta
import boto3

s3 = boto3.resource('s3')
date = datetime.now()
s3.meta.client.upload_file('data/processed/mobility_reports.csv', "sdd-s3-bucket", 'google_mobility_reports/{}/{}/{}/{}'.format(str(date.year).zfill(4),
                                                                           str(date.month).zfill(2),
                                                                           str(date.day).zfill(2),
                                                                           str(date.hour).zfill(2)))
