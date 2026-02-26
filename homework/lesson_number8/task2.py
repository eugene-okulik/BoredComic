import sys
sys.set_int_max_str_digits(1000000) # Добавил чтобы питон не ругался


def fibonacci():
    num1 = 0
    num2 = 1

    while True:
        yield num1

        num3 = num1 + num2
        num1 = num2
        num2 = num3


count = 0

for i in fibonacci():
    if count in {5, 200, 1000, 100000}:
        print(i)
    count += 1
