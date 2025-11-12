# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bid_List = {}

def amount():
    name_input = input("Whats your name\n")
    bid_input = int(input("How much do you want to bid? only integers please\n"))

    bid_List[name_input] = bid_input
    print("\n" * 5)


while input("Do you want to bid write yes \n") == "yes":
    amount()


max_score = 0
winner = ""

print(bid_List)
for key in bid_List:
    if bid_List[key] > max_score:
        winner = key
        max_score = bid_List[key]

print("Winner is " + str(winner) + " with an amount of" + str(max_score) + "€")


