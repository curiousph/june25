import math

def calculate_roots(numbers):
    """
    Given a list of numbers, returns a list of tuples with (number, square root, cube root).
    """
    results = []
    for num in numbers:
        sqrt = math.sqrt(num) if num >= 0 else float('nan')
        cbrt = math.copysign(abs(num) ** (1/3), num)
        results.append((num, sqrt, cbrt))
    return results

if __name__ == "__main__":
    try:
        user_input = input("Enter a number or a sequence of numbers separated by spaces: ")
        numbers = [float(x) for x in user_input.strip().split()]
        roots = calculate_roots(numbers)
        for num, sqrt, cbrt in roots:
            print(f"Number: {num}, Square Root: {sqrt}, Cube Root: {cbrt}")
    except ValueError:
        print("Please enter valid numbers.")
    except Exception as e:  
        print(f"An error occurred: {e}")