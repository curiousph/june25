# This program checks whether a given number is a palindrome.

def is_palindrome_number(n):
    """
    Returns True if the integer n is a palindrome, False otherwise.
    """
    original = str(n)
    reversed_num = original[::-1]
    return original == reversed_num

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to check if it is a palindrome: "))
        if is_palindrome_number(num):
            print(f"{num} is a palindrome.")
        else:
            print(f"{num} is not a palindrome.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
# Example usage
    print("Example checks:")
    examples = [121, -121, 12321, 12345]
    for example in examples:
        if is_palindrome_number(example):
            print(f"{example} is a palindrome.")
        else:
            print(f"{example} is not a palindrome.")