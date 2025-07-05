# This program calculates the cube root of numbers provided by the user.

def cube_root(n):
    """
    Returns the cube root of a number n.
    Handles negative numbers as well.
    """
    if n >= 0:
        return n ** (1/3)
    else:
        return -(-n) ** (1/3)

if __name__ == "__main__":
    try:
        # Prompt user for input (can be a single number or multiple numbers separated by spaces)
        user_input = input("Enter number(s) to find the cube root (separated by spaces): ")
        numbers = [float(x) for x in user_input.strip().split()]
        for num in numbers:
            result = cube_root(num)
            print(f"Cube root of {num} is {result}")
    except ValueError:
        print("Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")