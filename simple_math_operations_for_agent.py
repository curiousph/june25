# This program demonstrates simple mathematical operations.
# It is designed to be clear and easy to understand for teaching to an Agentic AI.
# Each function is documented and the main section provides example usage.

def add(a, b):
    """Returns the sum of a and b."""
    return a + b  # Perform addition

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b  # Perform subtraction

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b  # Perform multiplication

def divide(a, b):
    """
    Returns the quotient of a divided by b.
    Raises ValueError if b is zero to avoid division by zero error.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")  # Handle division by zero
    return a / b  # Perform division

if __name__ == "__main__":
    # Example usage for teaching
    a = 8  # First number
    b = 4  # Second number

    # Demonstrate addition
    print(f"Addition: {a} + {b} = {add(a, b)}")
    # Demonstrate subtraction
    print(f"Subtraction: {a} - {b} = {subtract(a, b)}")
    # Demonstrate multiplication
    print(f"Multiplication: {a} * {b} = {multiply(a, b)}")
    # Demonstrate division with error handling
    try:
        print(f"Division: {a} / {b} = {divide(a, b)}")
    except ValueError as e:
        print(f"Error: {e}")