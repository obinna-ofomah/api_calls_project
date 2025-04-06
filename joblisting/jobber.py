import os

import awswrangler as wr
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

AWS_BUCKET_NAME = os.getenv('AWS-BUCKET-NAME')
base_url = 'https://jobicy.com/api/v2/remote-jobs'
roles_url = f'{base_url}?count=20&geo=usa&industry=marketing&tag=seo'
response = requests.get(roles_url)
roles_data = response.json()['jobs']

managerial_roles = []
senior_roles = []

for role in roles_data:
    if 'Manager' in role['jobTitle']:
        managerial_roles.append(role['jobTitle'])

    if 'Senior' in role['jobTitle'] or 'Sr.' in role['jobTitle']:
        senior_roles.append(role['jobTitle'])


profiles_url = 'https://randomuser.me/api/?results=500'
profiles_data = requests.get(profiles_url).json()['results']

males_profile = []
females_profile = []
dates_of_birth = []
full_names = []

for profile in profiles_data:
    # appending the dates_of_birth for each profile
    dates_of_birth.append(profile['dob']['date'])

    # appending the concatenated full name into a list
    first_name = profile['name']['first']
    last_name = profile['name']['last']
    full_name = first_name + ' ' + last_name
    full_names.append(full_name)

    # Spliting the profiles into males and females
    if profile['gender'] == 'female':
        females_profile.append(profile)
    elif profile['gender'] == 'male':
        males_profile.append(profile)

folder = 'job_applicant_data_folder'

df_managers = pd.DataFrame({
    'managerial_roles': managerial_roles
})

wr.s3.to_parquet(
    df=df_managers,
    path=f"s3://{AWS_BUCKET_NAME}/{folder}/managerial_roles.parquet",
    dataset=False
)

df_seniors = pd.DataFrame({
    'senior_roles': senior_roles
})

wr.s3.to_parquet(
    df=df_seniors,
    path=f"s3://{AWS_BUCKET_NAME}/{folder}/senior_roles.parquet",
    dataset=False
)

df_full_profile = pd.DataFrame({
    'fullname': full_names,
    'date_of_birth': dates_of_birth
})

wr.s3.to_parquet(
    df=df_full_profile,
    path=f"s3://{AWS_BUCKET_NAME}/{folder}/applicants_profile.parquet",
    dataset=False
)

df_male_profiles = pd.DataFrame(
    {'males': males_profile}
)

wr.s3.to_parquet(
    df=df_male_profiles,
    path=f"s3://{AWS_BUCKET_NAME}/{folder}/male_profile.parquet",
    dataset=False
)

df_female_profiles = pd.DataFrame({
    'females': females_profile
})

wr.s3.to_parquet(
    df=df_female_profiles,
    path=f"s3://{AWS_BUCKET_NAME}/{folder}/female_profile.parquet",
    dataset=False
)

df_dob = pd.DataFrame({
    'date_of_birth': dates_of_birth
})

wr.s3.to_parquet(
    df=df_dob,
    path=f"s3://{AWS_BUCKET_NAME}/{folder}/date_of_birth.parquet",
    dataset=False
)

df_fullnames = pd.DataFrame({
    'fullname': full_names
})

wr.s3.to_parquet(
    df=df_fullnames,
    path=f"s3://{AWS_BUCKET_NAME}/{folder}/applicants_fullname.parquet",
    dataset=False
)
