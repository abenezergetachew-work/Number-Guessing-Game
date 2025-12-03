import random


number = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess > number:
            print("number to high, try again")

        elif guess < number:
            print("number to low, try again")

        else:
            print(f"You Got It!!! the number was {number}")
            break

    except ValueError:
        print("Invalid input")
