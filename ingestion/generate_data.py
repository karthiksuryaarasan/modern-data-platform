import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

fake = Faker()
random.seed(42)
np.random.seed(42)

RAW_PATH = "../raw_zone"

os.makedirs(RAW_PATH, exist_ok=True)


def generate_users(n=10000):
    users = []

    for i in range(n):
        signup_date = fake.date_between(start_date='-2y', end_date='-1y')
        users.append({
            "user_id": i,
            "name": fake.name(),
            "email": fake.email(),
            "country": fake.country(),
            "signup_date": signup_date
        })

    return pd.DataFrame(users)


def generate_products(n=1000):
    categories = ["Electronics", "Clothing", "Home", "Sports"]

    products = []

    for i in range(n):
        products.append({
            "product_id": i,
            "product_name": fake.word().capitalize(),
            "category": random.choice(categories),
            "price": round(random.uniform(100, 5000), 2)
        })

    return pd.DataFrame(products)


def generate_orders(users_df, products_df, n=50000):
    orders = []

    start_date = datetime.now() - timedelta(days=365)

    for i in range(n):
        order_time = start_date + timedelta(minutes=random.randint(0, 525600))

        orders.append({
            "order_id": i,
            "user_id": random.choice(users_df["user_id"].values),
            "product_id": random.choice(products_df["product_id"].values),
            "quantity": random.randint(1, 5),
            "order_timestamp": order_time
        })

    return pd.DataFrame(orders)


if __name__ == "__main__":
    print("Generating users...")
    users = generate_users()

    print("Generating products...")
    products = generate_products()

    print("Generating orders...")
    orders = generate_orders(users, products)

    users.to_csv(f"{RAW_PATH}/users.csv", index=False)
    products.to_csv(f"{RAW_PATH}/products.csv", index=False)
    orders.to_csv(f"{RAW_PATH}/orders.csv", index=False)

    print("Data generation complete. Files stored in raw_zone/")