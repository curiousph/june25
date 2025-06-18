import math

def gcd(a, b):
    """Compute the Greatest Common Divisor (GCD) of two numbers."""
    while b:
        # Using the Euclidean algorithm 
        # to find the GCD
        # This is a classic algorithm that works by repeatedly replacing the larger number by the remainder of the division of the two numbers.
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the Least Common Multiple (LCM) of two numbers."""
    # The LCM can be calculated using the formula: LCM(a, b) = abs(a * b) // GCD(a, b)
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b) if a and b else 0

if __name__ == "__main__":
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"GCD (MCD) of {num1} and {num2} is: {gcd(num1, num2)}")
        print(f"LCM of {num1} and {num2} is: {lcm(num1, num2)}")
    except ValueError:
        print("Please enter valid integers.")
    except Exception as e:
        print(f"An error occurred: {e}")