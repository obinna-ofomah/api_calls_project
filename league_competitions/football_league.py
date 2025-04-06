import os

import awswrangler as wr
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

football_api = 'http://api.football-data.org/v4/competitions/'
football_response = requests.get(football_api)
competitions_data = football_response.json()['competitions']

AWS_BUCKET_NAME = os.getenv('AWS-BUCKET-NAME')
competition_list = []

for competition in competitions_data:
    competition_list.append(competition['name'])

df = pd.DataFrame({
    'football_leagues': competition_list
})

folder = 'league_competitions_data'
file_name = 'football_league.parquet'
wr.s3.to_parquet(
    df=df,
    path=f"s3://{AWS_BUCKET_NAME}/{folder}/{file_name}",
    dataset=False
)
