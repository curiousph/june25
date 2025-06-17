def compare_characters(char1, char2):
    """
    Compares two characters and returns the numerical (Unicode) value of the larger character.
    If both are equal, returns that value.
    """
    if len(char1) != 1 or len(char2) != 1:
        raise ValueError("Both inputs must be single characters.")

    if char1 > char2:
        return ord(char1)
    else:
        return ord(char2)

#Test cases for the compare_characters function
class TestCompareCharacters:
    # This class contains test cases for the compare_characters function.
    def run_tests(self):
        print("Running test cases for compare_characters...\n")
        # Test 1: char1 > char2
        assert compare_characters('b', 'a') == ord('b'), "Test 1 Failed"
        print("Test 1 Passed: 'b' vs 'a'")

        # Test 2: char2 > char1
        assert compare_characters('a', 'z') == ord('z'), "Test 2 Failed"
        print("Test 2 Passed: 'a' vs 'z'")

        # Test 3: char1 == char2
        assert compare_characters('x', 'x') == ord('x'), "Test 3 Failed"
        print("Test 3 Passed: 'x' vs 'x'")

        # Test 4: numbers as characters
        assert compare_characters('5', '3') == ord('5'), "Test 4 Failed"
        print("Test 4 Passed: '5' vs '3'")

        # Test 5: special characters
        assert compare_characters('@', '#') == ord('@'), "Test 5 Failed"
        print("Test 5 Passed: '@' vs '#'")

        # Test 6: invalid input (should raise ValueError)
        try:
            compare_characters('ab', 'c')
            print("Test 6 Failed: Did not raise ValueError for invalid input")
        except ValueError:
            print("Test 6 Passed: Raised ValueError for invalid input")

if __name__ == "__main__":
    # Run tests
    tester = TestCompareCharacters()
    tester.run_tests()

    # User input
    c1 = input("\nEnter first character: ")
    c2 = input("Enter second character: ")
    try:
        result = compare_characters(c1, c2)
        print(f"The numerical value of the larger character is: {result}")
    except ValueError as e:
        print(e)
# This script compares two characters and returns the Unicode value of the larger character.