print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n "))


if height >= 120:
    age = int(input("What is your age?\n"))
    if age < 12:
        print("You have to pay 5€")
    elif age < 18:
        print("You have to pay 7€")
    else:
        print("You have to pay 12€")
else:
    print("Sorry you have to grow taller before you can ride.")