"""
Objective: Create an application that takes a set as input from the user and
generates the power set of the given set. The application can have a web interface or use the terminal.

Requirements:
1) User Input: The application should allow the user to input a set.
2) Generate Power Set: The application should generate the power set of the given set.
3) Display Power Set: The application should display the power set to the user.
"""
from collections import deque

def BFS_powerset(arr):
    q = deque([''])
    for i in range(len(arr)):
        # limit level iteration to q size
        limit = len(q)
        for _ in range(limit):
            # pop & append subset and new subset for next level iteration
            subset = q.popleft()
            q.append(subset)
            new_subset = subset + arr[i]
            q.append(new_subset)
    return list(q)
def validateInput(arr):
    return list(set(arr))
def printer(result):
    print( "{",end="")
    for set in sorted(result):
        print("{"+set+"}" ,end=',')
    print("}")
result = BFS_powerset(validateInput(['a', 'b', 'c','a']))
printer(sorted(result))