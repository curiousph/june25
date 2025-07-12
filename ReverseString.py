# This program reverses a string entered by the user and includes test cases for validation.

def reverse_string(s):
    """
    Returns the reversed version of the input string s.
    """
    return s[::-1]

class TestReverseString:
    """
    Test class for reverse_string function.
    Includes various test cases to validate correctness.
    """
    def run_tests(self):
        print("Running reverse_string test cases...\n")
        # Test 1: Simple word
        assert reverse_string("hello") == "olleh", "Test 1 Failed"
        # Test 2: Empty string
        assert reverse_string("") == "", "Test 2 Failed"
        # Test 3: Palindrome
        assert reverse_string("madam") == "madam", "Test 3 Failed"
        # Test 4: Numbers and letters
        assert reverse_string("abc123") == "321cba", "Test 4 Failed"
        # Test 5: Spaces
        assert reverse_string("a b c") == "c b a", "Test 5 Failed"
        # Test 6: Special characters
        assert reverse_string("!@#") == "#@!", "Test 6 Failed"
        print("All test cases passed.\n")

if __name__ == "__main__":
    # Run tests
    tester = TestReverseString()
    tester.run_tests()

    # User input
    user_input = input("Enter a string to reverse: ")
    reversed_str = reverse_string(user_input)