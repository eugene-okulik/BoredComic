sentences = "результат работы программы: 200"


def extract_and_add(text, add_value=10):
    return int(text.split(": ")[-1]) + add_value


print(extract_and_add(sentences))
