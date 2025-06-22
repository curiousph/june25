# This program counts the number of uppercase and lowercase letters in a given string.

def count_case_letters(s):
    """
    Counts the number of uppercase and lowercase letters in the given string.
    Returns a tuple: (uppercase_count, lowercase_count)
    """
    uppercase_count = 0  # Counter for uppercase letters
    lowercase_count = 0  # Counter for lowercase letters
    for char in s:
        if char.isupper():  # Check if character is uppercase
            uppercase_count += 1
        elif char.islower():  # Check if character is lowercase
            lowercase_count += 1
    return uppercase_count, lowercase_count

if __name__ == "__main__":
    # Prompt user for input
    user_input = input("Enter a string: ")
    # Count uppercase and lowercase letters
    upper, lower = count_case_letters(user_input)
    # Display the results
    print(f"Number of uppercase letters: {upper}")
    print(f"Number of lowercase letters: {lower}")