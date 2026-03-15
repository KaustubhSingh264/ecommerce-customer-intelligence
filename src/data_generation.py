import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

NUM_ROWS = 10000
product_categories = [
    "Electronics",
    "Clothing",
    "Home",
    "Beauty",
    "Sports",
    "Books"
]

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

data = []

for i in range(NUM_ROWS):

    order = {
        "order_id": f"ORD{100000 + i}",
        "customer_id": f"CUS{random.randint(1000,9999)}",
        "customer_name": fake.name(),
        "city": fake.city(),
        "product_category": random.choice(product_categories),
        "price": round(random.uniform(100, 5000), 2),
        "quantity": random.randint(1,5),
        "payment_method": random.choice(payment_methods),
        "order_date": fake.date_between(start_date="-2y", end_date="today"),
        "delivery_days": random.randint(1,7),
        "rating": round(random.uniform(1,5),1)
    }

    data.append(order)
    data = []

for i in range(NUM_ROWS):

    order = {
        "order_id": f"ORD{100000 + i}",
        "customer_id": f"CUS{random.randint(1000,9999)}",
        "customer_name": fake.name(),
        "city": fake.city(),
        "product_category": random.choice(product_categories),
        "price": round(random.uniform(100, 5000), 2),
        "quantity": random.randint(1,5),
        "payment_method": random.choice(payment_methods),
        "order_date": fake.date_between(start_date="-2y", end_date="today"),
        "delivery_days": random.randint(1,7),
        "rating": round(random.uniform(1,5),1)
    }

    data.append(order)

    df = pd.DataFrame(data)

    for col in ["customer_name","rating"]:
        df.loc[df.sample(frac=0.05).index, col] = np.nan
    duplicates = df.sample(frac=0.02)
    df = pd.concat([df, duplicates])
    df.loc[df.sample(frac=0.03).index, "product_category"] = "electronics"

    df.to_csv("data/raw/ecommerce_raw.csv", index=False)
    print("Dataset generated successfully!")
    print("Shape:", df.shape)