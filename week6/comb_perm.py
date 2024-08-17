"""
Objective
Create an application that calculates permutations and combinations based on user input.
The application should allow the user to enter the values for n (total items) and r (items to be chosen or arranged)
and then display the results.

Requirements
The application should take two inputs from the user: (total items) and r (items to be chosen or arranged).
The application should calculate and display:
The number of permutations P(n, r)
The number of combinations C(n, r)
The application can be implemented as either a web application or a terminal application.

"""
import sys
import unittest


def validateInputs(n, r):
    if len(n) == 0: raise ValueError("n cannot be empty")
    if len(r) > len(n): raise ValueError("r must be a subset of n")
    n_map = dict()
    for item in n:
        n_map[item] = n_map.get(item, 0) + 1
    for item2 in r:
        if item2 not in n_map:
            raise ValueError("There is an item in r that doesn't exist in n")
        else:
            n_map[item2] -= 1
            if n_map[item2] < 0:
                raise ValueError("Set r need to be a subset of n")
    return n_map


def factorial_calc(n):
    if n < 2:
        return n
    return n * factorial_calc(n - 1)


def permutations(n, r):
    if n - r == 0: return factorial_calc(n)
    if r == 0 and n > 0: return 1
    if n - r == 0: return factorial_calc(n)
    return factorial_calc(n) // factorial_calc(n - r)


def combinations(n, r):
    if n - r == 0: return factorial_calc(n)
    if r == 0 and n > 0: return 1
    return factorial_calc(n) // (factorial_calc(r) * factorial_calc(n - r))


def main():
    try:
        if len(sys.argv) != 3:
            print("Provide 2 terminal inputs. Each input must have a comma to separate values ")
            sys.exit()
        input_1 = list(sys.argv[1].split(','))
        input_2 = list(sys.argv[2].split(','))
        validateInputs(input_1,input_2)

        print('Based on input n: {} and input r: {}'.format(input_1, input_2))
        print("The number of permutations P(n, r) = ", permutations(len(input_1), len(input_2)))
        print("The number of combinations C(n, r) = ", combinations(len(input_1), len(input_2)))
    except ValueError:
        raise
    except TypeError:
        raise


class Testing(unittest.TestCase):
    def test_factorial_func(self):
        self.assertEqual(factorial_calc(4), 24)
        self.assertEqual(factorial_calc(1), 1)

    def test_map_validator(self):
        inputValues = ['a', 'b', 'c']
        chooseValues = ['a']
        errorValues = ['a', 'a']
        self.assertEqual(validateInputs(inputValues, chooseValues), {'a': 0, 'b': 1, 'c': 1})
        self.assertRaises(ValueError, validateInputs, inputValues, errorValues)

    def test_permutations(self):
        self.assertEqual(permutations(4, 2), 12)
        self.assertEqual(permutations(4, 4), 24)
        self.assertEqual(permutations(4, 0), 1)

    def test_combinations(self):
        self.assertEqual(combinations(4, 2), 6)
        self.assertEqual(combinations(4, 4), 24)
        self.assertEqual(combinations(4, 0), 1)


if __name__ == "__main__":
    #$main()
    unittest.main()