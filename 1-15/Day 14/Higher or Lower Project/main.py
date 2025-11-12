
import game_data
import random


print("welcome to the higher or lower game\n")

def score_count(celebrity_1, celebrity_2):
    print(f"{celebrity_1['name']} has {celebrity_2['follower_count']} followers and {celebrity_2['name']} has {celebrity_2['follower_count']}")

def game(score):
    playing = True
    celebrity_1 = random.choice(game_data.data)
    celebrity_2 = random.choice(game_data.data)

    if celebrity_1 == celebrity_2:
        celebrity_2 = random.choice(game_data.data)

    while playing:

        while True:
            print(f"(1){celebrity_1['name']} or (2){celebrity_2['name']}")
            guess = input("Who do you think has more followers? 1 or 2\n")

            if celebrity_1['follower_count'] > celebrity_2['follower_count']:
                if guess == "1":
                    print("You are correct")
                    score_count(celebrity_1, celebrity_2)
                    score += 1
                    celebrity_2 = random.choice(game_data.data)
                    break
                if guess == "2":
                    print("You are not correct")
                    score_count(celebrity_1, celebrity_2)
                    print(f"Your score was {score}")
                    playing = False
                    break
            elif celebrity_1['follower_count'] < celebrity_2['follower_count']:
                if guess == "2":
                    print("You are correct")
                    score_count(celebrity_1, celebrity_2)
                    score += 1
                    celebrity_1 = celebrity_2
                    celebrity_2 = random.choice(game_data.data)
                    break
                if guess == "1":
                    print("You are not correct")
                    score_count(celebrity_1, celebrity_2)
                    print(f"Your score was {score}")
                    playing = False
                    break
            else:
                if guess == "2" or "1":
                    print("You are correct")
                    score_count(celebrity_1, celebrity_2)
                    score += 1
                    celebrity_1 = celebrity_2
                    celebrity_2 = random.choice(game_data.data)
                    break
                else:
                     print("invalid input")

game(0)
