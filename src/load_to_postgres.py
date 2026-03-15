import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("data/processed/ecommerce_validated.csv")

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

df.to_sql(
    name="ecommerce_transactions",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data successfully loaded into PostgreSQL!")