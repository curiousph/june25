def binary_search(arr, target):
    """
    Performs binary search on a sorted list 'arr' to find 'target'.
    Returns the index of 'target' if found, else -1.
    Prints intermediate steps for readability.
    """
    left, right = 0, len(arr) - 1
    step = 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        if arr[mid] == target:
            print(f"Target {target} found at index {mid}.")
            return mid
        elif arr[mid] < target:
            print(f"Target {target} is greater than arr[mid]={arr[mid]}. Moving right.")
            left = mid + 1
        else:
            print(f"Target {target} is less than arr[mid]={arr[mid]}. Moving left.")
            right = mid - 1
        step += 1
    print(f"Target {target} not found in the list.")
    return -1

class TestBinarySearch:
    def run_tests(self):
        print("Running binary search test cases...\n")
        # Test 1: Target in middle
        arr = [1, 2, 3, 4, 5]
        assert binary_search(arr, 3) == 2, "Test 1 Failed"
        print("Test 1 Passed: Target in middle")

        # Test 2: Target at start
        assert binary_search(arr, 1) == 0, "Test 2 Failed"
        print("Test 2 Passed: Target at start")

        # Test 3: Target at end
        assert binary_search(arr, 5) == 4, "Test 3 Failed"
        print("Test 3 Passed: Target at end")

        # Test 4: Target not in list
        assert binary_search(arr, 6) == -1, "Test 4 Failed"
        print("Test 4 Passed: Target not in list")

        # Test 5: Empty list
        assert binary_search([], 1) == -1, "Test 5 Failed"
        print("Test 5 Passed: Empty list")

        # Test 6: Single element, target present
        assert binary_search([10], 10) == 0, "Test 6 Failed"
        print("Test 6 Passed: Single element, target present")

        # Test 7: Single element, target absent
        assert binary_search([10], 5) == -1, "Test 7 Failed"
        print("Test 7 Passed: Single element, target absent")

        # Test 8: Large list
        arr = list(range(1000))
        assert binary_search(arr, 500) == 500, "Test 8 Failed"
        print("Test 8 Passed: Large list")

        # Test 9: Negative numbers
        arr = [-10, -5, 0, 5, 10]
        assert binary_search(arr, -5) == 1, "Test 9 Failed"
        print("Test 9 Passed: Negative numbers")

        # Test 10: Duplicate elements (returns first found index)
        arr = [1, 2, 2, 2, 3]
        result = binary_search(arr, 2)
        assert result in [1, 2, 3], "Test 10 Failed"
        print("Test 10 Passed: Duplicate elements")

        print("\nAll test cases passed.")

if __name__ == "__main__":
    # Run tests
    tester = TestBinarySearch()
    tester.run_tests()

    # User input
    try:
        arr_input = input("\nEnter sorted numbers separated by spaces: ")
        arr = [int(x) for x in arr_input.strip().split()]
        target = int(input("Enter the number to search for: "))
        index = binary_search(arr, target)
        if index != -1:
            print(f"{target} found at index {index}.")
        else:
            print(f"{target} not found in the list.")
    except ValueError:
        print("Please enter valid integers.")
