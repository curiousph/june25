def concatenate_strings(str1, str2):
    """
    Concatenates two strings and returns the result.
    """
    return str1 + str2

if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    result = concatenate_strings(s1, s2)
    print(f"Concatenated string: {result}")