def format_text(text, prefix="", suffix="", capitalize=False, max_length=None):
    """
    Format a string with optional prefix, suffix, capitalization, and length trimming.

    Parameters:
    - text (str): The main text to be formatted.
    - prefix (str, optional): Text to add at the beginning. Default is "".
    - suffix (str, optional): Text to add at the end. Default is "".
    - capitalize (bool, optional): If True, capitalize the text. Default is False.
    - max_length (int, optional): If set, trims the final result to this number of characters. Default is None.

    Returns:
    - str: The formatted text.

    Raises:
    - TypeError: If `text`, `prefix`, or `suffix` are not strings.
    - ValueError: If `max_length` is not None or a positive integer.

    Examples:
    >>> format_text("hello")
    'hello'

    >>> format_text("world", prefix=">> ", suffix=" <<")
    '>> world <<'

    >>> format_text("python", capitalize=True)
    'Python'

    >>> format_text("example", max_length=4)
    'exam'

    >>> format_text("data", prefix="[", suffix="]", capitalize=True, max_length=6)
    '[Data]'
    """
# Input validation
    if not isinstance(text, str):
        raise TypeError("The 'text' parameter must be a string.")
    if not isinstance(prefix, str):
        raise TypeError("The 'prefix' parameter must be a string.")
    if not isinstance(suffix, str):
        raise TypeError("The 'suffix' parameter must be a string.")
    if max_length is not None:
        if not isinstance(max_length, int) or max_length <= 0:
            raise ValueError("The 'max_length' parameter must be a positive integer or None.")

    # Apply capitalization
    if capitalize:
        text = text.capitalize()

    # Add prefix and suffix
    result = prefix + text + suffix

    # Truncate to max_length if needed
    if max_length is not None:
        text = text[:max_length]

    return result
    
#User Input Section
text = input("Enter the main text: ")
prefix = input("Enter a prefix (optional): ")
suffix = input("Enter a suffix (optional): ")
capitalize_input = input("Capitalize first letter? (yes/no): ").strip().lower()
capitalize = capitalize_input == "yes"
max_length_input = int(input("Max length (optional, press Enter to skip): "))

try:
    output = format_text(
        text , prefix=prefix , suffix=suffix, capitalize=capitalize,
        max_length=max_length_input if max_length_input else None
    )
    print("\nFormatted text:", output)
except Exception as e:
    print("Error:", e)
