import pandas as pd
from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "PaulObro!"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "local_market_pipeline"

csv_path = "data/raw/census/2026-05-06/census_demographics.csv"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

df = pd.read_csv(csv_path)

df.to_sql(
    "raw_census_demographics",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded Census data into PostgreSQL table: raw_census_demographics")
