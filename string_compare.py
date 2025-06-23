# This program compares two input strings and prints True if they match, otherwise False.

def compare_strings(str1, str2):
    """
    Returns True if both strings are exactly the same, otherwise False.
    """
    return str1 == str2

if __name__ == "__main__":
    # Prompt user for two strings
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    # Compare and display result
    result = compare_strings(s1, s2)
    print(f"Strings match: {result}")
    # Example usage
    print(compare_strings("hello", "hello"))  # True
    print(compare_strings("hello", "world"))  # False   