import random
import art

cards = {
"Ass of": {"♦️": 11, "♥️": 11, "♣️": 11, "♠️": 11},
"Two of": {"♦️": 2, "♥️": 2, "♣️": 2, "♠️": 2},
"Three of": {"♦️": 3, "♥️": 3, "♣️": 3, "♠️": 3},
"Four of": {"♦️": 4, "♥️": 4, "♣️": 4, "♠️": 4},
"Five of": {"♦️": 5, "♥️": 5, "♣️": 5, "♠️": 5},
"Six of": {"♦️": 6, "♥️": 6, "♣️": 6, "♠️": 6},
"Seven of": {"♦️": 7, "♥️": 7, "♣️": 7, "♠️": 7},
"Eight of": {"♦️": 8, "♥️": 8, "♣️": 8, "♠️": 8},
"Nine of": {"♦️": 9, "♥️": 9, "♣️": 9, "♠️": 9},
"Ten of": {"♦️": 10, "♥️": 10, "♣️": 10, "♠️": 10},
"Jack of": {"♦️": 10, "♥️": 10, "♣️": 10, "♠️": 10},
"Queen of": {"♦️": 10, "♥️": 10, "♣️": 10, "♠️": 10},
"King of": {"♦️": 10, "♥️": 10, "♣️": 10, "♠️": 10},
}

def pick_card(player):
    global cards
    global card_score

    typ = random.choice(list(cards.keys()))
    farbe = random.choice(list(cards[typ].keys()))
    card_score = cards[typ][farbe]

    if player == 1:
        safe_cards.append((typ, farbe,))
        return card_score, farbe, typ
    else:
        safe_cards_dealer.append((typ, farbe,))
        return card_score, farbe, typ

def calculate_score(hand):
    score = 0
    ass_count = 0
    for typ, farbe in hand:
        amount = cards[typ][farbe]
        score += amount
        if "Ass" in typ:
            ass_count += 1

    while score > 21 and ass_count > 0:
        score -= 10
        ass_count -= 1

    return score

def outcome():
    print("\n--- Final Outcome ---")
    player_sc()
    dealer_sc()
    if player_score > 21:
        print("You bust! dealer wins.")
    elif dealer_score > 21 or player_score > dealer_score:
        print("You win!")
    elif dealer_score == player_score:
        print("It's a draw!")
    else:
        print("dealer wins!")

def player_sc():
    global player_score
    player_score = calculate_score(safe_cards)
    print(f"Your cards: {safe_cards}\n Score = {player_score}")
def dealer_sc():
    global dealer_score
    dealer_score = calculate_score(safe_cards_dealer)
    print(f"dealer cards: {safe_cards_dealer}\n Score = {dealer_score}")

while input("Do you want to play a round of Blackjack? type y\n") == "y":
    print(art.logo)
    safe_cards = []
    safe_cards_dealer = []
    card_score = ""
    player_score = 0
    dealer_score = 0
    for _ in range(2):
        pick_card(0)
        pick_card(1)
    player_sc()
    dealer_sc()

    while player_score < 21:
        if dealer_score != 21:
            if input("Pick another card? type y") == "y":
                pick_card(1)
                player_score += card_score
                player_sc()
            else:
                while dealer_score < 17:
                    pick_card(0)
                    dealer_score += card_score
                    dealer_sc()
                break
        else:
            print("BLACKJACK! dealer wins")
            break

    if player_score == 21:
        print("BLACKJACK! You win")

    outcome()
else:
    print("Goodybe")
