# Program: Parentheses Validator
# Description: Checks if a string contains a valid sequence of parentheses (supports (), {}, []).
# Includes a test class with multiple test cases for valid and invalid scenarios.
# Author: GitHub Copilot
# Date: June 22, 2025

def is_valid_parentheses(s):
    """
    Returns True if the parentheses in the string are balanced, False otherwise.
    Ignores all non-parenthesis characters.
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack

class TestParenthesesValidator:
    """
    Test class for is_valid_parentheses function.
    Includes simple and complex test cases with alphanumeric and special characters.
    """
    def run_tests(self):
        print("Running parentheses validator test cases...\n")
        # Simple balanced cases
        assert is_valid_parentheses("()") == True, "Test 1 Failed"
        assert is_valid_parentheses("([])") == True, "Test 2 Failed"
        assert is_valid_parentheses("{[()]}") == True, "Test 3 Failed"
        # Simple unbalanced cases
        assert is_valid_parentheses("(") == False, "Test 4 Failed"
        assert is_valid_parentheses("([)]") == False, "Test 5 Failed"
        assert is_valid_parentheses("{[(])}") == False, "Test 6 Failed"
        # Complex with alphanumeric and symbols
        assert is_valid_parentheses("a+(b*[c-{d/e}])") == True, "Test 7 Failed"
        assert is_valid_parentheses("if (x > 0) { return [y]; } else { return (z); }") == True, "Test 8 Failed"
        assert is_valid_parentheses("function(a, b[2]) { return (a+b); }") == True, "Test 9 Failed"
        assert is_valid_parentheses("a+(b*[c-{d/e}]") == False, "Test 10 Failed"
        assert is_valid_parentheses("abc123") == True, "Test 11 Failed"  # No parentheses, considered balanced
        assert is_valid_parentheses("([a+b]*{c/d})") == True, "Test 12 Failed"
        assert is_valid_parentheses("([a+b]*{c/d}") == False, "Test 13 Failed"
        assert is_valid_parentheses(")(") == False, "Test 14 Failed"
        assert is_valid_parentheses("a(b)c)d(") == False, "Test 15 Failed"
        print("All test cases passed.\n")

if __name__ == "__main__":
    # Run tests
    tester = TestParenthesesValidator()
    tester.run_tests()

    # User input for validation
    user_input = input("Enter a string to validate parentheses: ")
    if is_valid_parentheses(user_input):
        print("Parentheses are balanced.")
    else:
        print("Parentheses are NOT balanced.")
