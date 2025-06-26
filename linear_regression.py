# This program implements a simple linear regression from scratch.
# It calculates the best-fit line (y = mx + c) for given data points.

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
    if n != len(y) or n == 0:
        raise ValueError("Input lists must have the same non-zero length.")

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = sum((x[i] - mean_x) ** 2 for i in range(n))

    if denominator == 0:
        raise ValueError("Variance of x is zero. Cannot compute slope.")

    m = numerator / denominator
    c = mean_y - m * mean_x
    return m, c

if __name__ == "__main__":
    # Example usage with user input
    try:
        x_input = input("Enter x values separated by spaces: ")
        y_input = input("Enter y values separated by spaces: ")
        x = [float(val) for val in x_input.strip().split()]
        y = [float(val) for val in y_input.strip().split()]
        m, c = linear_regression(x, y)
        print(f"Linear Regression Equation: y = {m:.4f}x + {c:.4f}")
    except Exception as e:
        print(f"Error: {e}") 