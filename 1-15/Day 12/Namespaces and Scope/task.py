enemies = 1
drinkpotion = 0

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

def drink():
    global drinkpotion
    drinkpotion = 2
    print(f"drink potion: {drinkpotion}")
    return drinkpotion

drink()
print(drinkpotion)