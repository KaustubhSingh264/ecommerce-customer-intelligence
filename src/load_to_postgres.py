import pandas as pd
from sqlalchemy import create_engine

# Step 1: Load dataset
df = pd.read_csv("data/processed/ecommerce_validated.csv")

# Step 2: PostgreSQL connection
engine = create_engine(
    "postgresql://postgres:ROHIT264@localhost:5432/ecommerce_analytics"
)

# Step 3: Load dataframe into PostgreSQL
df.to_sql(
    name="ecommerce_transactions",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Data successfully loaded into PostgreSQL!")