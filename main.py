"""
Author: Meng Moua
Course: CSC500
Assignment: Module 1, Part 1
"""

def main():
    num1 = input("Enter num1: ")
    num2 = input("Enter num2: ")
    print('Their sum:')
    print(f'\t{num1} + {num2} =', add(num1, num2))
    print('Their subtraction results:')
    print(f'\tResult1: {num1} - {num2} =', subtract(num1, num2))
    print(f'\tResult2: {num2} - {num1} =', subtract(num2, num1))
    print('Their difference:', difference(num1, num2))

def add(num1, num2) -> str:
    """
    Add two numbers
    :param num1: number 1
    :param num2: number 2
    :return: a result as string
    """
    if not valid_number(num1) or not valid_number(num2):
        return "Invalid input number(s)"

    return str(int(num1) + int(num2))

def difference(num1, num2) -> str:
    """
    Difference of two numbers
    :param num1: number 1
    :param num2: number 2
    :return: a result as string
    """
    if not valid_number(num1) or not valid_number(num2):
        return "Invalid input number(s)"

    if int(num1) > int(num2):
        return str(int(num1) - int(num2))

    return str(int(num2) - int(num1))

def subtract(num1, num2) -> str:
    """
    Subtract two numbers
    :param num1: number 1
    :param num2: number 2
    :return: a result as string
    """
    if not valid_number(num1) or not valid_number(num2):
        return "Invalid input number(s)"

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
