



def my_function():
    print("Hello World")
    print("Bye")

my_function()


def right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if not wall_in_front():
        move()
    else:
        if wall_in_front():
            turn_left()
            if wall_in_front():
                turn_left()
            else:
                move()
                right()

        else:
            move()
            right()
