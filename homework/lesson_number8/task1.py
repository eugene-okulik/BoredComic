import random

salary = int(input("Enter your salary: "))

bonus = random.choice([True, False])

if bonus:
    random_bonus = random.randint(500, 5000)
    salary_with_bonus = salary + random_bonus
    print(f"{salary}, {bonus} - ${salary_with_bonus}")
else:
    print(f"{salary}, {bonus} - ${salary}")
