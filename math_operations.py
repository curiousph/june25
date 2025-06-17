# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

class TestMathOperations:
    def run_tests(self):
        print("Running 100 test cases for MathOperations...\n")
        passed = 0
        failed = 0

        # 100 diverse test datasets: (a, b)
        test_data = [
            (1, 2), (0, 0), (-1, 1), (100, 200), (3.5, 2.5), (-5, -10), (1e6, 1e6), (0.1, 0.2), (999, -999), (50, 0),
            (2, -2), (123456, 654321), (3.1415, 2.7182), (-1000, 1000), (7, 8), (0, -1), (1, 0), (0, 1), (-1, 0),
            (1.1, 2.2), (5, 5), (10, -10), (0.5, 0.5), (100, -100), (9999, 1), (1, 9999), (123, 321), (0.333, 0.667),
            (-50, 50), (2.5, -2.5), (1000, 0.001), (0.001, 1000), (42, 42), (7, -7), (-7, 7), (0, 100), (100, 0),
            (1e-6, 1e-6), (1e6, -1e6), (-1e6, 1e6), (12345, 54321), (0.123, 0.321), (1, -1), (-1, 1), (2, 2), (3, 3),
            (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15),
            (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26),
            (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37),
            (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48),
            (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59)
        ]

        for idx, (a, b) in enumerate(test_data, 1):
            try:
                assert add(a, b) == a + b
                assert subtract(a, b) == a - b
                assert multiply(a, b) == a * b
                if b != 0:
                    assert divide(a, b) == a / b
                else:
                    try:
                        divide(a, b)
                        print(f"Test {idx} Failed: divide({a}, {b}) did not raise ValueError")
                        failed += 1
                        continue
                    except ValueError:
                        pass
                passed += 1
            except AssertionError:
                print(f"Test {idx} Failed: ({a}, {b})")
                failed += 1

        print(f"\nTests completed. Passed: {passed}, Failed: {failed}")

if __name__ == "__main__":
    # Run tests
    tester = TestMathOperations()
    tester.run_tests()

    # User input
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    print(f"Addition: {add(num1, num2)}")
    print(f"Subtraction: {subtract(num1, num2)}")
    print(f"Multiplication: {multiply(num1, num2)}")
    try:
        print(f"Division: {divide(num1, num2)}")
    except ValueError as e:
        print(e)