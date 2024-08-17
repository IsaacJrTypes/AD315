import random
from collections import Counter

# Task 1: Simulating Coin Tosses
def coin_toss_simulation():
    tosses = [random.choice(['H', 'T']) for _ in range(100)]
    results = dict(Counter(tosses))
    print(f"Coin Toss Results: {results}")

# Task 2: Rolling a Die
def die_roll_simulation():
    rolls = [random.randint(1, 6) for _ in range(60)]
    results = dict(Counter(rolls))
    print(f"Die Roll Sim (60 rolls): {results}")

# Task 3: Drawing Cards
def card_draw_simulation():
    deck = ['R']*26 + ['B']*26
    random.shuffle(deck)
    draws = [deck.pop() for _ in range(20)]
    results = dict(Counter(draws))
    print("Card Draw Sim (20 draws):", results)

# Task 4: Probability of Compound Events
def two_coin_flip_simulation():
    outcomes = []
    both_heads = 0
    one_heads = 0
    for _ in range(50):
        flip1 = random.choice(['H', 'T'])
        flip2 = random.choice(['H', 'T'])
        outcome = flip1 + flip2
        outcomes.append(outcome)
        if outcome == 'HH':
            both_heads+=1
        if outcome == 'TH' or outcome == 'HT':
            one_heads+=1
    results = dict(Counter(outcomes))
    print(f"Two Coin Flip Sim (1000 simulations):", results)
    print(f"Both Heads: {both_heads}, Atleast One Heads: {one_heads}")

def main():
    coin_toss_simulation()
    die_roll_simulation()
    card_draw_simulation()
    two_coin_flip_simulation()

if __name__ == "__main__":
   main()