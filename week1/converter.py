"""
Input:

A number in its original base.
The base of the input number (between 2 and 16).
The base to which the number should be converted (between 2 and 16).
Output:

The converted number in the specified base.
Interface:

A simple terminal-based user interface is required.
Optionally, you can create a web or mobile front-end interface.
Testing:

Test the program with various inputs to ensure it handles all cases correctly.
"""
import unittest


def check_value(value):
    if not value.isdigit() and ord('a') <= ord(value.lower()) <= ord('f'):
        return ord(value.lower()) - 87
    if value.isdigit():
        return int(value)
    else:
        raise ValueError(f"Invalid character '{value}' for base conversion")


def validate_number(num, base_in):
    for element in num:
        if check_value(element) >= base_in:
            print(f"Invalid digit '{element}' for base {base_in}")
            return False
    return True


# convert any base to base 10
def base_10_converter(num, base_in):
    sum = 0
    for i in range(len(num)):
        digit = check_value(num[i])
        calc = digit * (base_in ** (len(num) - 1 - i))
        sum += calc
    return sum


# convert base 10 to any target base
def target_base_converter(num: int, base_out: int):
    if num == 0:
        return "0"
    value = num
    remainder = ''

    while value > 0:
        remainder = str(value % base_out) + remainder
        value //= base_out
    return remainder


def base_converter(num, base_in, base_out):
    base_10_num = base_10_converter(num, base_in)
    converted_num = target_base_converter(base_10_num, base_out)
    return converted_num


def main():
    try:
        print("Let's convert a number from it's base input to a desired base")
        num = input("Enter the number: ")
        base_in = int(input("Enter the base of the input number: "))
        base_out = int(input("Enter the base to convert to: "))
        if base_in < 2 or base_in > 16 or base_out < 2 or base_out > 16:
            print("Bases must be between 2 and 16.")
            return
        if validate_number(num, base_in):
            converted_num = base_converter(num, base_in, base_out)
            print(f"The number {num} in base {base_in} is {converted_num} in base {base_out}.")
    except:
        raise


class Testing(unittest.TestCase):
    def test_check_value_func(self):
        self.assertEqual(check_value('1'), 1)
        with self.assertRaises(ValueError):
            check_value('I')

    def test_validate_number(self):
        self.assertFalse(validate_number("102",2))
        self.assertTrue(validate_number("a02",11))

    def test_base_converter(self):
        self.assertEqual(base_converter("a103",11,13),"6165")
        self.assertEqual(base_converter("0",9,13),"0")

if __name__ == "__main__":
    main()
    #unittest.main()