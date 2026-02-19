
senteces = "результат работы программы: 200"


def some_word(num):
    return int(num.split(": ")[-1]) + 10


print(some_word(senteces))

