def calculate(*args, **kwargs):
    """
    Parameters:
    *args: Positional arguments, expected to be numbers (int or float).
    **kwargs: Keyword arguments representing operations to apply:
        - add (bool): If True, perform addition.
        - subtract (bool): If True, perform subtraction.
        - multiply (bool): If True, perform multiplication.
        - divide (bool): If True, perform division.

    Returns:
    A dictionary with operation names as keys and results as values.

    Raises:
    ValueError: If less than two numeric arguments are provided or if input types are invalid.
    ZeroDivisionError: If division by zero occurs.
    """
    if not args:
        raise ValueError("At least one number is required.")
    if not all(isinstance(x, (int, float)) for x in args):
        raise ValueError("All arguments must be numbers (int or float).")
    if len(args) < 2:
        raise ValueError("At least two numbers are required for calculations.")

    return process_operations(args, kwargs)


def process_operations(numbers, operations):
    """
    Helper function to apply operations to the provided numbers.

    Parameters:
    numbers (tuple): A tuple of numbers.
    operations (dict): Dictionary with operation flags (e.g., add=True).

    Returns:
    dict: Results of the operations.
    """
    results = {}
    a_iter = iter(numbers)
    first = next(a_iter)

    if operations.get('add'):
        results['Addition'] = sum(numbers)

    if operations.get('subtract'):
        result = first
        for num in a_iter:
            result -= num
        results['Subtraction'] = result

    a_iter = iter(numbers)
    first = next(a_iter)
    if operations.get('multiply'):
        result = first
        for num in a_iter:
            result *= num
        results['Multiplication'] = result

    a_iter = iter(numbers)
    first = next(a_iter)
    if operations.get('divide'):
        result = first
        for num in a_iter:
            if num == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result /= num
        results['Division'] = result

    if not results:
        raise ValueError("No valid operations selected.")

    return results


def get_user_input():
    """
    This will collect numeric input and operation choices from the user.
    """
    try:
        numbers_input = input("Enter numbers separated by space: ")
        numbers = list(map(float, numbers_input.strip().split()))
        if len(numbers) < 2:
            raise ValueError("You must enter at least two numbers.")

        # Ask which operations to perform
        print("Which operations would you like to perform?")
        add = input("Add? (yes/no): ").strip().lower() == 'yes'
        subtract = input("Subtract? (yes/no): ").strip().lower() == 'yes'
        multiply = input("Multiply? (yes/no): ").strip().lower() == 'yes'
        divide = input("Divide? (yes/no): ").strip().lower() == 'yes'

        results = calculate(*numbers, add=add, subtract=subtract, multiply=multiply, divide=divide)
        print("\nResults:")
        for op, value in results.items():
            print(f"{op}: {value}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    get_user_input()
