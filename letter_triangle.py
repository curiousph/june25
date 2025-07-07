# This program prints an equilateral triangle of letters based on the user's input number.
# For example, input 3 will print:
#   A
#  BB
# CCC

def print_letter_equilateral_triangle(n):
    """
    Prints an equilateral triangle where the i-th row contains the i-th uppercase letter repeated i times,
    centered to form an equilateral triangle.
    """
    for i in range(1, n + 1):
        letter = chr(64 + i)  # 65 is 'A' in ASCII
        row = letter * i
        print(row.center(n + (n - 1)))  # Center the row for equilateral shape

if __name__ == "__main__":
    try:
        num = int(input("Enter the size of the triangle: "))
        if num < 1 or num > 26:
            print("Please enter a number between 1 and 26.")
        else:
            print_letter_equilateral_triangle(num)
    except ValueError:
        print("Please enter a valid integer.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     # Example usage
#     print("Example triangle with size 5:")
#     print_letter_equilateral_triangle(5)
#     # This will print:

#        A
#       BB
#      CCC
#     DDDD
#    EEEEE
#     # Note: The maximum size is 26 to fit the uppercase English alphabet.
#     # If the user inputs a number greater than 26, it will prompt them to