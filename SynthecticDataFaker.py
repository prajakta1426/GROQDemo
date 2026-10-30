
from faker import Faker
fake = Faker('en_IN') 
#Faker.seed(42)

for i in range(5):
    print(f"User {i+1}:")
    print(fake.name())
    print(fake.address())
    print(fake.email())
    print(fake.phone_number())
    print(fake.date_of_birth(minimum_age=18, maximum_age=60))
    print(fake.iban())
    print(fake.credit_card_number(card_type='visa'))
    print(fake.text())
    print(fake.android_platform_token())
    print(fake.aadhaar_id)
    print('---')
