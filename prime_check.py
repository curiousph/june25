import math

def is_prime(n):
    """
    Efficiently checks if a number is prime.
    Returns True if prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

class TestIsPrime:
    def run_tests(self):
        print("Running test cases for is_prime...\n")
        # Negative number (should not be prime)
        assert is_prime(-10) == False, "Test Failed: Negative number"
        # Zero (should not be prime)
        assert is_prime(0) == False, "Test Failed: Zero"
        # One (should not be prime)
        assert is_prime(1) == False, "Test Failed: One"
        # Two (smallest prime)
        assert is_prime(2) == True, "Test Failed: Two (smallest prime)"
        # Three (prime)
        assert is_prime(3) == True, "Test Failed: Three (prime)"
        # Four (even, not prime)
        assert is_prime(4) == False, "Test Failed: Four (even, not prime)"
        # Five (prime)
        assert is_prime(5) == True, "Test Failed: Five (prime)"
        # Nine (3*3, not prime)
        assert is_prime(9) == False, "Test Failed: Nine (3*3, not prime)"
        # Thirteen (prime)
        assert is_prime(13) == True, "Test Failed: Thirteen (prime)"
        # Twenty-five (5*5, not prime)
        assert is_prime(25) == False, "Test Failed: Twenty-five (5*5, not prime)"
        # Twenty-nine (prime)
        assert is_prime(29) == True, "Test Failed: Twenty-nine (prime)"
        # Ninety-seven (prime)
        assert is_prime(97) == True, "Test Failed: Ninety-seven (prime)"
        # Hundred (not prime)
        assert is_prime(100) == False, "Test Failed: Hundred (not prime)"
        # Hundred and one (prime)
        assert is_prime(101) == True, "Test Failed: Hundred and one (prime)"
        # 121 (11*11, not prime)
        assert is_prime(120) == False, "Test Failed: 121 (11*11, not prime)"
        # 9973 (prime)
        assert is_prime(9973) == True, "Test Failed: 9973 (prime)"
        # 9999 (not prime)
        assert is_prime(9999) == False, "Test Failed: 9999 (not prime)"
        # 104729 (large prime)
        assert is_prime(104729) == True, "Test Failed: 104729 (large prime)"
        # 104730 (large non-prime)
        assert is_prime(104730) == False, "Test Failed: 104730 (large non-prime)"
        print("All test cases passed.")

if __name__ == "__main__":
    # Run tests
    tester = TestIsPrime()
    tester.run_tests()

    try:
        num = int(input("\nEnter a number: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer")
    except Exception as e:
        print(f"An error occurred: {e}")