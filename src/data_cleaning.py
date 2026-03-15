import pandas as pd 
import numpy as np

pd.set_option('display.max_columns',None)

df = pd.read_csv("data/raw/ecommerce_raw.csv") 

#VIEWING FIRST 5 ROWS
print(df.head())

#NUMBER OOF ROWS AND COLUMN
print("DISPLAY SHAPE",df.shape)

#IDENTIFY THE MISSING VALUES
print(df.info())

#SHOWS STASTICAL VALUES
print(df.describe())

#MISSING VALUES CHECKING
print("Missing values:")
print(df.isnull().sum())

#CHECKING DUPLICATE ROWS
print("Duplicate rows:", df.duplicated().sum())
 

#UNIQUE CATEGORIES
print("Product categories:")
print(df["product_category"].unique())


print("Data profiling completed.")

                                              #DATA CLEANING
# REMOVE DUPLICATE ROWS
print("Duplicate rows before cleaning:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicate rows after cleaning:", df.duplicated().sum())

# MISSING VALUE 
print("Missing values before cleaning:")
print(df.isnull().sum())

df["customer_name"] = df["customer_name"].fillna("Unknown")

df["rating"] = df["rating"].fillna(df["rating"].mean())

#Standardize Category Names

df["product_category"] = df["product_category"].str.title()

#Validate Numeric Columns
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

#REMOVE IN VALID ROWS
df = df[df["price"] > 0]
df = df[df["quantity"] > 0]

# Final Data Check
print("Final dataset shape:", df.shape)
print("Remaining missing values:")
print(df.isnull().sum())


#Save Cleaned Dataset
df.to_csv("data/processed/ecommerce_cleaned.csv", index=False)

print("Clean dataset saved successfully.")

