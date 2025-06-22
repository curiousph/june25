# Program: Parentheses Validator
# Description: Checks if a string contains a valid sequence of parentheses (supports (), {}, []).
# Includes a test class with multiple test cases for valid and invalid scenarios.
# Author: GitHub Copilot
# Date: June 22, 2025

def is_valid_parentheses(s):
    """
    Checks if the input string 's' has valid parentheses sequence.
    Supports (), {}, []. Returns True if valid, False otherwise.
    """
    stack = []  # Stack to keep track of opening brackets
    mapping = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets
    for char in s:
        if char in mapping.values():  # If it's an opening bracket
            stack.append(char)
        elif char in mapping:  # If it's a closing bracket
            # If stack is empty or top of stack doesn't match
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()  # Pop the matching opening bracket
    return not stack  # If stack is empty, all brackets matched

class TestParenthesesValidation:
    def run_tests(self):
        print("Running parentheses validation test cases...\n")
        # Test 1: Simple valid
        assert is_valid_parentheses("()") == True, "Test 1 Failed"
        print("Test 1 Passed: ()")
        # Test 2: Nested valid
        assert is_valid_parentheses("([])") == True, "Test 2 Failed"
        print("Test 2 Passed: ([])")
        # Test 3: Multiple types valid
        assert is_valid_parentheses("{[()]}[]") == True, "Test 3 Failed"
        print("Test 3 Passed: {[()]}[]")
        # Test 4: Invalid order
        assert is_valid_parentheses("(]") == False, "Test 4 Failed"
        print("Test 4 Passed: (]")
        # Test 5: Unmatched open
        assert is_valid_parentheses("((") == False, "Test 5 Failed"
        print("Test 5 Passed: ((")
        # Test 6: Unmatched close
        assert is_valid_parentheses(")(") == False, "Test 6 Failed"
        print("Test 6 Passed: )(")
        # Test 7: Empty string
        assert is_valid_parentheses("") == True, "Test 7 Failed"
        print("Test 7 Passed: Empty string")
        # Test 8: Complex valid
        assert is_valid_parentheses("{[()()[]]}([])") == True, "Test 8 Failed"
        print("Test 8 Passed: {[()()[]]}([])")
        # Test 9: Complex invalid
        assert is_valid_parentheses("{[(])}") == False, "Test 9 Failed"
        print("Test 9 Passed: {[(])}")
        # Test 10: Only open/close
        assert is_valid_parentheses("((((((((((" ) == False, "Test 10 Failed"
        print("Test 10 Passed: ((((((((((")
        print("\nAll test cases passed.")

if __name__ == "__main__":
    # Run tests
    tester = TestParenthesesValidation()
    tester.run_tests()

    # User input
    s = input("\nEnter a string of parentheses to validate: ")
    if is_valid_parentheses(s):
        print("The sequence is valid.")
    else:
        print("The sequence is NOT valid.")
