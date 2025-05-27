"""
- Display art
-generate a random account from the game data
-Format the account data into a printable format
-Ask user for a guess
- Check if user is correct
- get follower count of each account
- use if statement to check who has more followers
- score keeping
-make the game repeatable
-making account at position B become the next account at position A
"""

from art import logo
from game_data import data
import random
print(logo)
account_a = random.choice(data)
account_b = random.choice(data)


