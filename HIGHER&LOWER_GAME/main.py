from art import logo
from art import vs
from game_data import data
import random

print(logo)
score = 0


def format(account):
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]
    return f"{account_name} a {account_des} , from {account_country}"


def check_answer(user_guess, follower_a, follower_b):
    if follower_a > follower_b:
        return user_guess == "a"
    else:
        return user_guess == "b"


account_b = random.choice(data)
continu = True
while continu:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    # print(account_a)

    print(f"Compare A: {format(account_a)}")
    print(vs)
    print(f"Against B: {format(account_b)}")

    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]
    # print(follower_count_a)
    # print(follower_count_b)

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_check = check_answer(guess, follower_count_a, follower_count_b)

    if is_check:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"your final score is {score}")
        print("Thank you for playing this game")
        continu = False