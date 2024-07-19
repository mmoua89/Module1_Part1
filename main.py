"""
Author: Meng Moua
Course: CSC500-1
Assignment: Part 1
    - Write a Python program to find the addition and subtraction of two numbers.
    - Ask the user to input two numbers (num1 and num2). Given those two numbers,
      add them together to find the output. Also, subtract the two numbers to find the output.
"""

# Main driver
def main():
    num1 = input("Enter num1: ")
    num2 = input("Enter num2: ")
    print('Their sum:', add(num1, num2))
    print('Their subtraction results:')
    print('\tResult1:', subtract(num1, num2))
    print('\tresult2:', subtract(num2, num1))
    print('Their difference:', difference(num1, num2))

def add(num1, num2):
    """
    Add two numbers
    :param num1: number 1
    :param num2: number 2
    :return: a result as string
    """
    if not valid_number(num1) or not valid_number(num2):
        return "Invalid input numbers"

    return str(int(num1) + int(num2))

def difference(num1, num2):
    if not valid_number(num1) or not valid_number(num2):
        return "Invalid input numbers"

    if int(num1) > int(num2):
        return str(int(num1) - int(num2))

    return str(int(num2) - int(num1))

def subtract(num1, num2):
    """
    Subtract two numbers
    :param num1: number 1
    :param num2: number 2
    :return: a result as string
    """
    if not valid_number(num1) or not valid_number(num2):
        return "Invalid input numbers"

    return str(int(num1) - int(num2))

def valid_number(num) -> bool:
    """
    Validate a number
    :param num: number
    :return: true or false
    """
    try:
        int(num)
    except ValueError:
        return False
    return True

if __name__ == '__main__':
    main()
