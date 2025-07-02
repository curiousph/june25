# This program converts a given string to a number (integer or float) if possible.

def string_to_number(s):
    """
    Tries to convert the input string to an integer or float.
    Returns the number if successful, otherwise raises a ValueError.
    """
    try:
        # Try converting to integer first
        return int(s)
    except ValueError:
        try:
            # If integer conversion fails, try float
            return float(s)
        except ValueError:
            raise ValueError("Input string cannot be converted to a number.")

if __name__ == "__main__":
    user_input = input("Enter a string to convert to a number: ")
    try:
        number = string_to_number(user_input)
        print(f"Converted value: {number} (type: {type(number).__name__})")
    except ValueError as e:
        print(f"Error: {e}")