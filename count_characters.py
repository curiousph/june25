# This program counts the number of characters in a string input by the user.

def count_characters(s):
    """
    Returns the number of characters in the given string.
    """
    return len(s)

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    count = count_characters(user_input)
    print(f"Number of characters in the string: {count}")   