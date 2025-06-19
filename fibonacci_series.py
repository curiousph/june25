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

class TestFibonacciSeries:
    def run_tests(self):
        print("Running Fibonacci series tests...\n")
        # Test 1: n = 0
        assert fibonacci_series(0) == [], "Test 1 Failed"
        print("Test 1 Passed: n = 0")

        # Test 2: n = 1
        assert fibonacci_series(1) == [0], "Test 2 Failed"
        print("Test 2 Passed: n = 1")

        # Test 3: n = 2
        assert fibonacci_series(2) == [0, 1], "Test 3 Failed"
        print("Test 3 Passed: n = 2")

        # Test 4: n = 5
        assert fibonacci_series(5) == [0, 1, 1, 2, 3], "Test 4 Failed"
        print("Test 4 Passed: n = 5")

        # Test 5: n = 10
        assert fibonacci_series(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "Test 5 Failed"
        print("Test 5 Passed: n = 10")

        # Test 6: negative n
        assert fibonacci_series(-5) == [], "Test 6 Failed"
        print("Test 6 Passed: n = -5")

        print("\nAll tests passed.")

if __name__ == "__main__":
    # Run tests
    tester = TestFibonacciSeries()
    tester.run_tests()

    # User input
    try:
        num = int(input("\nEnter the number of terms for Fibonacci series: "))
        result = fibonacci_series(num)
        print(f"Fibonacci series with {num} terms: {result}")
    except ValueError:
        print("Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")