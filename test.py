from faker import Faker

fake = Faker(locale='zh_CN')

print(fake.name())
print(fake.address())
print(fake.country())
print(fake.user_agent())
print(fake.chrome())

