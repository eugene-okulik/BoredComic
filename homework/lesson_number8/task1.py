import random

salary = int(input("Enter your salary: "))
bonus = random.choice([True, False])

if bonus:
    random_bonus = random.randrange(5000, 25000)
    salary += random_bonus
    print(f"${salary}")
else:
    print(f"${salary}")
