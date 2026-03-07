import sys
sys.set_int_max_str_digits(1000000)


def fibonacci():
    num = 0
    num2 = 1

    while True:
        next_num = num + num2
        num = num2
        num2 = next_num

        yield num


count = 0

for number in fibonacci():
    count += 1

    if count in {5, 200, 1000, 100000}:
        print(number)

    if count == 100000:
        break
