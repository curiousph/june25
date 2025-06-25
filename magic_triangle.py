# This program checks if the given 3x3 triangle (represented as a list of 3 lists)
# is a "magic triangle" where the sum of the numbers on each side is equal.

def is_magic_triangle(triangle):
    """
    Checks if the input 3x3 triangle is a magic triangle.
    The triangle should be represented as a list of 3 lists, each with 3 numbers.
    Returns True if the sum of numbers on each side is equal, False otherwise.
    """
    if len(triangle) != 3 or any(len(row) != 3 for row in triangle):
        raise ValueError("Input must be a 3x3 triangle (list of 3 lists, each with 3 numbers).")

    # The triangle's sides are:
    # Side 1: triangle[0][0], triangle[0][1], triangle[0][2]
    # Side 2: triangle[0][2], triangle[1][1], triangle[2][0]
    # Side 3: triangle[2][0], triangle[2][1], triangle[2][2]
    side1 = triangle[0][0] + triangle[0][1] + triangle[0][2]
    side2 = triangle[0][2] + triangle[1][1] + triangle[2][0]
    side3 = triangle[2][0] + triangle[2][1] + triangle[2][2]

    return side1 == side2 == side3

if __name__ == "__main__":
    print("Enter the numbers for the magic triangle (3 rows, 3 numbers each):")
    triangle = []
    try:
        for i in range(3):
            row = list(map(int, input(f"Row {i+1}: ").strip().split()))
            if len(row) != 3:
                raise ValueError("Each row must have exactly 3 numbers.")
            triangle.append(row)
        if is_magic_triangle(triangle):
            print("This is a magic triangle!")
        else:
            print("This is NOT a magic triangle.")
    except Exception as e:
        print(f"Error: {e}")
    # Example usage
    print("Example triangle:")
    example_triangle = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ]
    if is_magic_triangle(example_triangle):
        print("This is a magic triangle!")
    else:
        print("This is NOT a magic triangle.")