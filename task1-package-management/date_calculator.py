from datetime import datetime

SUPPORTED_FORMATS = [
    "%Y-%m-%d",   # 2025-07-13
    "%d/%m/%Y",   # 23/05/2024
    "%m-%d-%Y"    # 15-03-2025
]

def check_date(date_str):
    """
    Attempt to parse a date string using known formats.

    Parameters:
    - date_str (str): The date string to parse.

    Returns:
    - datetime: A datetime object representing the date.

    Raises:
    - ValueError: If no supported formats match.
    """
    for a in SUPPORTED_FORMATS:
        try:
            return datetime.strptime(date_str, a)
        except ValueError:
            continue
    raise ValueError(
        f"Invalid date format: '{date_str}'. Supported formats include: "
        f"{', '.join(SUPPORTED_FORMATS)}"
    )

def calculate_date_difference(date1, date2):
    """
    Calculate the number of days between two dates.

    Parameters:
    - date1 (str): The first date string.
    - date2 (str): The second date string.

    Returns:
    - int: The absolute number of days between the two dates.

    Raises:
    - ValueError: If the provided dates are not in the correct format.

    
    """
    date_1 = check_date(date1)
    date_2 = check_date(date2)
    return abs((date_2 - date_1).days)


    # Example usage with user input
print("Enter two dates (accepted formats: YYYY-MM-DD, DD/MM/YYYY, MM-DD-YYYY):")
date1_input = input("First date: ")
date2_input = input("Second date: ")

try:
    difference = calculate_date_difference(date1_input, date2_input)
    print(f"The difference between the dates is {difference} days.")
except ValueError as error:
    print(f"Error: {error}")