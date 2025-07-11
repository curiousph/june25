# This program sorts a list of numbers entered by the user using the bubble sort algorithm.

def bubble_sort(numbers):
    """
    Sorts a list of numbers in ascending order using bubble sort.
    """
    n = len(numbers)
    for i in range(n):
        # Traverse the list from 0 to n-i-1
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

if __name__ == "__main__":
    try:
        # Prompt user for input
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [float(x) for x in user_input.strip().split()]
        sorted_numbers = bubble_sort(numbers)
        print("Sorted numbers:", sorted_numbers)
    except ValueError:
        print("Please enter valid numbers separated by spaces.")