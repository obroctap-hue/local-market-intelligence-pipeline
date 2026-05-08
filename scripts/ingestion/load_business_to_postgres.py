import pandas as pd
from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "PaulObro"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "local_market_pipeline"

csv_path = "data/raw/business/zip_business_patterns.csv"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

df = pd.read_csv(csv_path, dtype={"zip": str, "naics": str})

df.to_sql(
    "zip_business_patterns_raw",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded business data into PostgreSQL table: zip_business_patterns_raw")
print(df.head())