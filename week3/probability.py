"""
Task 1: Implementing the Dice Roll Function

Write a Python function that simulates rolling M number of N-sided dice once and returns the sum of the outcomes.

Task 2: Simulating Multiple Rolls

Create a function to simulate rolling M number of N-sided dice K times and record the results.

Task 3: Calculating Probability Distribution

Write a function to calculate the probability of each possible sum when M number of N-sided dice are rolled.

Task 4: User Interface

Allow the user to input the values of N, M, K and display the probability distribution.
"""
import random
import itertools

def die_roll(m,n,k=1):
    repeat_rolls = [[random.randint(1, n) for num in range(m)] for num in range(k)]
    return repeat_rolls

# find all valid permutations of sum based on n-side and m number of die
def dice_sum_permutations(m, n, target):
    valid_perms = []
    all_perms = itertools.product(range(1, n+1), repeat=m)
    for perm in all_perms:
        #print(perm)
        perm_sum = sum(perm)
        if perm_sum == target:
            valid_perms.append(perm)
    return valid_perms

def calculate_probability_distribution(m, n):
    possible_outcomes = n**m
    prob_map = {}
    for possible_sum in range(m, m*n+1):
        perms = dice_sum_permutations(m, n, possible_sum)
        prob_map[possible_sum] = len(perms) / possible_outcomes
    return prob_map

def main():
    m = int(input("Enter number of dice: "))
    n = int(input("Enter number of sides on each die: "))
    k = int(input("Enter number of rolls: "))

    rolls = die_roll(m, n, k)
    print(f"You rolled {m} number of dices with {n} sides dice {k} times ")

    prob_dist = calculate_probability_distribution(m, n)
    print("Probability Distribution:")
    for sum_val, probability in prob_dist.items():
        print(f"Sum {sum_val}: {probability:.4f}")

if __name__ == "__main__":
    main()