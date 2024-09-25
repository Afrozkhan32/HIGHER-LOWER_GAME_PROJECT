# HIGHER-LOWER_GAME_PROJECT

This Python code implements a simple game where players guess which of two social media accounts has more followers. Let's break it down step by step.

### Imports
```python
from art import logo
from art import vs
from game_data import data
import random
```
- **art**: Imports visual elements like logos or separators to enhance user experience.
- **game_data**: Imports a dataset called `data`, which contains information about various social media accounts.
- **random**: A module to generate random numbers and select random elements.

### Game Initialization
```python
print(logo)
score = 0
```
- Displays the game logo.
- Initializes a variable `score` to keep track of the player’s correct answers.

### Helper Function: `format()`
```python
def format(account):
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]
    return f"{account_name} a {account_des} , from {account_country}"
```
- This function takes an account dictionary as input and formats its information (name, description, country) into a string for easy reading.

### Answer Check Function: `check_answer()`
```python
def check_answer(user_guess, follower_a, follower_b):
    if follower_a > follower_b:
        return user_guess == "a"
    else:
        return user_guess == "b"
```
- This function checks if the user's guess (either 'a' or 'b') is correct based on the follower counts of the two accounts.
- It returns `True` if the guess is correct and `False` otherwise.

### Game Loop
```python
account_b = random.choice(data)
continu = True
while continu:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format(account_a)}")
    print(vs)
    print(f"Against B: {format(account_b)}")

    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_check = check_answer(guess, follower_count_a, follower_count_b)

    if is_check:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"your final score is {score}")
        print("Thank you for playing this game")
        continu = False
```

1. **Random Selection**: The game starts by randomly selecting an account for `account_b`.
2. **Loop Control**: A `while` loop continues as long as `continu` is `True`, meaning the game will keep running until the player answers incorrectly.
3. **Account Selection**:
   - The current `account_a` is set to `account_b`, and a new `account_b` is selected.
   - If `account_a` and `account_b` are the same, a new `account_b` is selected to ensure they are different.
4. **Display Information**: The game displays information about the two accounts for comparison.
5. **User Input**: The player is prompted to guess which account has more followers by entering 'a' or 'b'.
6. **Answer Check**: The player's guess is checked using the `check_answer` function.
7. **Score Update**:
   - If the guess is correct, the score is incremented, and the current score is displayed.
   - If incorrect, the game ends, and the final score is shown.

### Conclusion
This code creates an engaging game that tests the player's knowledge of social media accounts based on follower counts. It features random selection, user interaction, and keeps track of scores, providing a fun way to learn about various accounts.
