# This program sorts a list of numbers entered by the user using the efficient built-in Timsort algorithm (used by Python's sorted()).

def sort_numbers(numbers):
    """
    Sorts a list of numbers in ascending order using Python's efficient built-in sorting algorithm.
    """
    return sorted(numbers)

if __name__ == "__main__":
    try:
        # Prompt user for input
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [float(x) for x in user_input.strip().split()]
        sorted_numbers = sort_numbers(numbers)
        print("Sorted numbers:", sorted_numbers)
    except ValueError:
        print("Please enter valid numbers separated by spaces.")