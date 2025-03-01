import random
import uuid
from faker import Faker

fake = Faker()

# Define the structure of claims data
def generate_account_record():
    return {
        "AccountNo": fake.bothify(text='??#########').upper(),
        "FirstName": fake.first_name(),
        "LastName": fake.last_name(),
        "StreetAddress": fake.street_address(),
        "CityAddress": fake.city(),
        "State": fake.state_abbr(),
        "Zip": fake.zipcode(),
        "Email": fake.email(),
        "Gender": fake.random_element(elements=('M', 'F')),
        "Phone": fake.phone_number(),
        "DOB": fake.date_of_birth(minimum_age=18, maximum_age=90),        
        "MonthlyPayment": round(random.uniform(300, 900), 2),
        "DaysLate": fake.random_element(elements=(0, 30, 60, 90)),
    }

# Define the structure of your data
def generate_data():
    return {
        #"id": random.randint(1000, 9999),
        "id": str(uuid.uuid4()),  # Generate a GUID
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address().replace("\n", ", "),
        "phone": fake.phone_number(),
        "dob": fake.date_of_birth(minimum_age=18, maximum_age=90),
        "balance": round(random.uniform(1000, 100000), 2),
        "created_at": fake.date_time_this_decade(),
    }

if __name__ == "__main__":
    ...