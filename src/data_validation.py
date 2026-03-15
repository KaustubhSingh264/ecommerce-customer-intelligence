import pandas as pd
import numpy as np

df = pd.read_csv("data/processed/ecommerce_cleaned.csv")

#INSPECTING NUMERIC COLUMN
print(df.describe())

#Detect Outliers Using IQR

#We will use the IQR (Interquartile Range) method.

Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)

IQR = Q3 - Q1

# Calculate Outlier Limits
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify Outliers
outliers = df[(df["price"] < lower_bound) | (df["price"] > upper_bound)]

print("Number of price outliers:", outliers.shape[0])

#Remove Price Outliers
df = df[(df["price"] >= lower_bound) & (df["price"] <= upper_bound)]

#Validate Quantity Values
df = df[(df["quantity"] >= 1) & (df["quantity"] <= 10)]

#Final Data Check
print("Dataset shape after validation:", df.shape)

df.to_csv("data/processed/ecommerce_validated.csv", index=False)

print("Validated dataset saved successfully.")
