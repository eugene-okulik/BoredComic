num = 10
user_guess = int(input("Guess a number: "))

while True:
    if user_guess == num:
        print("Correct!")
        break
    else:
        print("Wrong!")
        user_guess = int(input("Let's try again: "))
