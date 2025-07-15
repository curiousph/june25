# This program returns the rowIndex-th (0-indexed) row of Pascal's triangle.

def get_pascals_triangle_row(rowIndex):
    """
    Returns the rowIndex-th row of Pascal's triangle as a list.
    """
    row = [1]
    for i in range(1, rowIndex + 1):
        # Compute next value using previous row values (from right to left to avoid overwriting)
        row.append(1)
        for j in range(i - 1, 0, -1):
            row[j] = row[j] + row[j - 1]
    return row

if __name__ == "__main__":
    try:
        rowIndex = int(input("Enter the row index for Pascal's triangle: "))
        result = get_pascals_triangle_row(rowIndex)
        print(f"Row {rowIndex} of Pascal's Triangle: {result}")
    except ValueError:
        print("Please enter a valid