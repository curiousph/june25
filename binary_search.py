# This program implements the binary search algorithm from scratch.
# It includes a function to perform binary search on a sorted list,
# prints the intermediate steps for clarity, and contains a test class
# with various test cases to validate the implementation.

def binary_search(arr, target):
    """
    Performs binary search on a sorted list 'arr' to find 'target'.
    Prints intermediate steps for clarity.
    Returns the index of 'target' if found, else returns -1.
    """
    left = 0
    right = len(arr) - 1

    step = 1  # Step counter for printing
    while left <= right:
        mid = (left + right) // 2
        # Print the current search range and middle element
        print(f"Step {step}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        if arr[mid] == target:
            print(f"Target {target} found at index {mid}.\n")
            return mid  # Target found
        elif arr[mid] < target:
            print(f"Target {target} is greater than arr[mid]={arr[mid]}. Searching right half.\n")
            left = mid + 1  # Continue search in right half
        else:
            print(f"Target {target} is less than arr[mid]={arr[mid]}. Searching left half.\n")
            right = mid - 1  # Continue search in left half
        step += 1

    print(f"Target {target} not found in the list.\n")
    return -1  # Target not found

class TestBinarySearch:
    """
    Test class for binary_search function.
    Contains multiple test cases to validate correctness.
    """
    def run_tests(self):
        print("Running binary search test cases...\n")
        # Test 1: Target present in the middle
        arr = [1, 3, 5, 7, 9]
        assert binary_search(arr, 5) == 2, "Test 1 Failed"
        # Test 2: Target present at the beginning
        assert binary_search(arr, 1) == 0, "Test 2 Failed"
        # Test 3: Target present at the end
        assert binary_search(arr, 9) == 4, "Test 3 Failed"
        # Test 4: Target not present
        assert binary_search(arr, 4) == -1, "Test 4 Failed"
        # Test 5: Empty list
        assert binary_search([], 1) == -1, "Test 5 Failed"
        # Test 6: Single element, target present
        assert binary_search([10], 10) == 0, "Test 6 Failed"
        # Test 7: Single element, target absent
        assert binary_search([10], 5) == -1, "Test 7 Failed"
        # Test 8: Large list, target present
        large_arr = list(range(0, 1000, 2))  # Even numbers from 0 to 998
        assert binary_search(large_arr, 200) == 100, "Test 8 Failed"
        # Test 9: Large list, target absent
        assert binary_search(large_arr, 201) == -1, "Test 9 Failed"
        # Test 10: Negative numbers
        arr_neg = [-10, -5, 0, 5, 10]
        assert binary_search(arr_neg, -5) == 1, "Test 10 Failed"
        print("All test cases passed.\n")

if __name__ == "__main__":
    # Run tests
    tester = TestBinarySearch()
    tester.run_tests()

    # User input for demonstration
    try:
        # Prompt user for a sorted list of integers
        user_input = input("Enter sorted numbers separated by spaces: ")
        arr = [int(x) for x in user_input.strip().split()]
        # Prompt user for the target value to search
        target = int(input("Enter the number to search for: "))
        # Perform binary search and print intermediate steps
        result = binary_search(arr, target)
        if result != -1:
            print(f"Result: {target} found at index {result}.")
        else:
            print(f"Result: {target} not found in the list.")
    except ValueError:
        print("Please enter valid integers for the list and target number.")
