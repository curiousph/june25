# This program implements simple linear regression from scratch.
# It calculates the best-fit line (y = mx + c) for a set of data points provided by the user.
# The program includes detailed commentary to explain each step of the calculation.

def linear_regression(x, y):
    """
    Calculates the slope (m) and intercept (c) for the best-fit line using linear regression.
    Args:
        x (list of float): Independent variable values.
        y (list of float): Dependent variable values.
    Returns:
        tuple: (slope, intercept)
    """
    n = len(x)
    # Check if input lists are valid
    if n != len(y) or n == 0:
        raise ValueError("Input lists must have the same non-zero length.")

    # Calculate the mean of x and y
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    # Calculate the numerator and denominator for the slope (m)
    # Numerator: sum of (x_i - mean_x) * (y_i - mean_y)
    # Denominator: sum of (x_i - mean_x)^2
    numerator = 0
    denominator = 0
    for i in range(n):
        numerator += (x[i] - mean_x) * (y[i] - mean_y)
        denominator += (x[i] - mean_x) ** 2

    # If denominator is zero, all x values are the same (vertical line)
    if denominator == 0:
        raise ValueError("Variance of x is zero. Cannot compute slope.")

    # Calculate slope (m)
    m = numerator / denominator
    # Calculate intercept (c)
    c = mean_y - m * mean_x
    return m, c

if __name__ == "__main__":
    # Example usage with user input
    try:
        # Prompt user to enter x values
        x_input = input("Enter x values separated by spaces: ")
        # Prompt user to enter y values
        y_input = input("Enter y values separated by spaces: ")
        # Convert input strings to lists of floats
        x = [float(val) for val in x_input.strip().split()]
        y = [float(val) for val in y_input.strip().split()]
        # Calculate linear regression coefficients
        m, c = linear_regression(x, y)
        # Display the resulting equation
        print(f"Linear Regression Equation: y = {m:.4f}x + {c:.4f}")
    except Exception as e:
        # Handle errors (e.g., invalid input, zero variance)
        print(f"Error: {e}")