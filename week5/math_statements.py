"""
Objectives:
Implement logical operations (AND, OR, NOT, IF...THEN, IF AND ONLY IF) in a program.
Create a user interface (web or terminal) to accept inputs for A and B.
Display the results of the logical operations based on user inputs.
Generate a truth table showing all possible values of A and B and the results of logical operations.

"""


def conjunction(a, b):
    return a and b


def disjunction(a, b):
    return a or b


def negation(a):
    return not a


def implication(p, q):
    return not p or q


def biconditional(a, b):
    return a == b

def print_rows():
    for a, b in [(True, True), (True, False), (False, True), (False, False)]:
        print((' {:<6} |' * 8).format(a, negation(a), b, negation(b), conjunction(a, b), disjunction(a, b),
                                      implication(a, b), biconditional(a, b)))
def main():
    try:
        user_choice = input("Input any of the two digit entries (00 01 10 11) to find a truth: ")
        if user_choice not in ['00','01', '10', '11']:
            raise ValueError('Input value can only be one of the two digit entries')
        user_choice = [*user_choice]
        a,b = int(user_choice[0]),int(user_choice[1])

        print(" P = {} , Q = {}".format(a, b))
        print("Now that we know what is true and what is not, lets see how logical operations can help reveal the truth")
        print("Conjunction(P,Q) => {}".format(conjunction(a, b)))
        print("Disjunction(P,Q) => {}".format(disjunction(a, b)))
        print("Negation(P) = {}, negation(Q) = {}".format(negation(a), negation(b)))
        print("Implication(P,Q) => {}".format(implication(a, b)))
        print("Biconditional(P,Q) => {}".format(biconditional(a, b)))

        print("Generate Truth Table")
        print("1 = True, 0 = False")
        print((' {:<6} |' * 8).format('P', '!(P)', 'Q', '!(Q)', 'P ∧ Q', 'P ∨ Q', 'P => Q', 'P <=> Q'))
        print('=' * 70)
        print_rows()
    except ValueError as e:
        print(f"Error: {e}")

main()