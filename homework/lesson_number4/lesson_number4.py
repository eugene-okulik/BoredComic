# Task 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

print(name, last_name, city, phone, country)

# Task 2

text = "Здесь написано какой-то текст: 20"

string_index = text.index(':') + 2

print(int(text[string_index:]) + 10)

# Task 3

students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

students_str = ', '.join(students)
subjects_str = ', '.join(subjects)

text = f'Students {students_str}, study these subjects: {subjects_str}'
print(text)



