def fibonacci_series(n):
    """
    Generates a list containing the Fibonacci series up to n terms.
    """
    if n <= 0:
        return []
    series = [0]
    if n == 1:
        return series
    series.append(1)
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series

if __name__ == "__main__":
    try:
        num = int(input("Enter the number of terms for Fibonacci series: "))
        result = fibonacci_series(num)
        print(f"Fibonacci series with {num} terms: {result}")
    except ValueError:
        print("Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")