# This program calculates the square root of a number provided by the user.

import math

def square_root(n):
    """
    Returns the square root of a non-negative number n.
    Raises a ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(n)

if __name__ == "__main__":
    try:
        # Prompt user for input
        user_input = input("Enter a number to find the square root: ")
        num = float(user_input)
        result = square_root(num)
        print(f"Square root of {num} is {result}")
    except ValueError as e:
        print(f"Error: {e}")