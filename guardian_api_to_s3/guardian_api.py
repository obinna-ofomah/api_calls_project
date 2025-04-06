import os

import awswrangler as wr
import boto3
import pandas as pd
import requests as re
from dotenv import load_dotenv

load_dotenv()

matched_results = []
query = 'Nigeria | nigeria'
API_KEY = os.getenv('API-KEY')
AWS_ACCESS_KEY = os.getenv('AWS-ACCESS-KEY')
AWS_SECRET_KEY = os.getenv('AWS-SECRET-KEY')
AWS_BUCKET_NAME = os.getenv('AWS-BUCKET-NAME')


web_title = []
web_url = []


def guardian_scrapper(pages):
    base_url = 'https://content.guardianapis.com/search?api-key'
    date = 'from-date=2025-01-01'
    size = 'page-size=20'
    for page in range(1, pages + 1):
        base_url = f'{base_url}={API_KEY}&q={query}&{size}&{date}&page={page}'
        response = re.get(base_url)
        if response.status_code == 200:
            data = response.json()['response']['results']
            for item in data:
                matched_results.append(item)
        else:
            print(f'No data found in {page}')

    return matched_results


def convert_results_to_df(list_items):
    for element in list_items:
        web_title.append(element['webTitle'])
        web_url.append(element['webUrl'])

    df = pd.DataFrame({
        'web_title': web_title,
        'web_url': web_url
    })

    return df


matched_data = guardian_scrapper(10)
df = convert_results_to_df(matched_data)


s3_client = boto3.client('s3')
response = s3_client.create_bucket(
    Bucket=AWS_BUCKET_NAME,
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-2'
    },
)

wr.s3.to_parquet(
    df=df,
    path=f"s3://{AWS_BUCKET_NAME}/guardian_api_data/guardian_data.parquet",
    dataset=False
)
