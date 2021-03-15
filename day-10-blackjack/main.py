import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def play():
    user_cards = random.sample(cards,2)
    comp_cards = random.sample(cards,2)
    print(f"User cards: {user_cards}")
    print(f"Comp cards: {comp_cards}")

play()
