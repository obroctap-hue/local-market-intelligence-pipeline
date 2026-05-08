import os
from datetime import datetime

import pandas as pd
import requests


url = "https://api.census.gov/data/2023/acs/acs5?get=NAME,B01003_001E,B19013_001E&for=zip%20code%20tabulation%20area:*"

response = requests.get(url)
response.raise_for_status()

data = response.json()

df = pd.DataFrame(data[1:], columns=data[0])

df = df.rename(columns={
    "B01003_001E": "population",
    "B19013_001E": "median_income",
    "zip code tabulation area": "zip_code"
})

today = datetime.today().strftime("%Y-%m-%d")
folder = f"data/raw/census/{today}"
os.makedirs(folder, exist_ok=True)



file_path = f"{folder}/census_demographics.csv"
df.to_csv(file_path, index=False)

print(f"Saved Census data to {file_path}")
print(df.head())