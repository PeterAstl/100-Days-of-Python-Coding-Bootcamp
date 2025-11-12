
import art
#
# print (art.logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


key = {"+": add,
       "-": sub,
       "*": mul,
       "/": div,
}


def is_number():

    while True:
        second_number = input("What's your second number? ").strip()
        if second_number == "":
            print("Empty input is not allowed.")
            continue
        try:
            number_2 = int(second_number)
            return number_2
        except ValueError:
            print("Invalid input. Please enter a valid number.")


while True:
    start = input("Hello, what number do you want? ")
    try:
        number_1 = int(start)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")


while True:
    key_input = input("What do you want to do? +,-,/,*")
    if  key_input == "+":
        number_2 = is_number()
        add(number_1, number_2)
        print(f"Your Number is: {add(number_1, number_2)} ")
        break
    elif key_input == "-":
        number_2 = is_number()
        sub(number_1, number_2)
        print(f"Your Number is: {sub(number_1, number_2)} ")
        break
    elif  key_input == "*":
        number_2 = is_number()
        mul(number_1, number_2)
        print(f"Your Number is: {mul(number_1, number_2)} ")
        break
    elif  key_input == "/":
        number_2 = is_number()
        div(number_1, number_2)
        print(f"Your Number is: {div(number_1, number_2)} ")
        break

    else:
        print("Invalid input. Please enter a valid symbol.")
