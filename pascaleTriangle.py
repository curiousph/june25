# This program generates the first numRows of Pascal's triangle.
# Each number in the triangle is the sum of the two numbers directly above it.

def generate_pascals_triangle(numRows):
    """
    Returns the first numRows of Pascal's triangle as a list of lists.
    """
    triangle = []
    for row in range(numRows):
        # Start each row with 1
        current_row = [1]
        if triangle:
            last_row = triangle[-1]
            # Compute the values between the 1s
            for i in range(1, row):
                current_row.append(last_row[i-1] + last_row[i])
            # End each row with 1
            current_row.append(1)
        triangle.append(current_row)
    return triangle

if __name__ == "__main__":
    try:
        numRows = int(input("Enter the number of rows for Pascal's triangle: "))
        result = generate_pascals_triangle(numRows)
        print("Pascal's Triangle:")
        for row in result:
            print(row)
    except ValueError:
        print("Please enter a valid integer.")