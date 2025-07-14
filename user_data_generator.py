# user_data_generator: 👉 Module to generate fake user info

from faker import Faker
import random

def generate_user_data():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = f"{first_name.lower()}.{last_name.lower()}{random.randint(100, 999)}"
    password = fake.password(length=12)
    return {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "password": password
    }
