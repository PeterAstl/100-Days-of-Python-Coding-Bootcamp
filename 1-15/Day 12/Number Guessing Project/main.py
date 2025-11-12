import random

def game(hp):
    attempts = hp
    print(f"You have {attempts} attempts left")
    while True:
        guess = int(input("Guess again\n"))

        if number == guess:
            print("You guessed right!")
            break
        else:
            if attempts > 1:
                if guess > number:
                    attempts -= 1
                    print(f"Your guess is too high.\n")
                    print(f"You have {attempts} attempts left")
                elif guess < number:
                    attempts -= 1
                    print(f"Your guess is too low.")
                    print(f"You have {attempts} attempts left")
            else:
                print("You loose.\n the correct number is " + str(number))
                break


while True:
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    x = input("choose a difficulty\n easy, hard\n")

    number = random.randint(1, 100)
    if x == "easy":
        game(10)
    else:
        game(5)

