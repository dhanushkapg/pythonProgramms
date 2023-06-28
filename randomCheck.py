import random

def game_A():
    capital = 1000
    for _ in range(1000):
        if random.random() < 0.49:  # biased coin flip, tails with p=0.49
            capital += 1
        else:
            capital -= 1
    return capital

def game_B():
    capital = 1000
    for _ in range(1000):
        if capital % 3 == 0:
            if random.random() < 0.09:  # first coin, tails with p1=0.09
                capital += 1
            else:
                capital -= 1
        else:
            if random.random() < 0.74:  # second coin, tails with p2=0.74
                capital += 1
            else:
                capital -= 1
    return capital

num_games = 1000000
total_capital = 0

for _ in range(num_games):
    if random.random() < 0.5:  # balanced coin flip
        total_capital += game_A()
    else:
        total_capital += game_B()

average_capital = total_capital / num_games
if average_capital > 1000:
    status = "Winner"
elif average_capital < 1000:
    status = "Loser"
else:
    status = "Break-even"

print("Game Status:", status)