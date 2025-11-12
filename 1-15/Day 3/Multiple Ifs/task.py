print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n "))


if height >= 120:
    print("you can ride the roller coaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("Children tickets are 5$")
        pay = 5
    elif age < 18:
        print("Youth tickets are 7$")
        pay = 7
    else:
        print("Adult tickets are 12$")
        pay = 12

    foto = input("Do you want a Foto?\n")
    if foto == "yes":
        pay += 3

    print("your final bill is gonna be " + str(pay) + " $")


else:
    print("You are too short to ride")
