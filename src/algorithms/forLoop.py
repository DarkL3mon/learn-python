from time import time

def format_and_validate_input(numbers):
    """Convert input into a validated string of digits."""
    # Ensure that the input is converted to a string
    formatted = (
        "".join(str(n) for n in numbers)
        if isinstance(numbers, (list, tuple, set))
        else str(numbers)
    )

    # Validate that the input contains only numeric digits
    if not formatted.isdigit():
        raise ValueError("Input contains non-numeric characters")

    return formatted

def sum_all_digits(numbers):
    """Return the sum of all individual digits."""
    total = 0

    # Format and validate the input numbers
    formatted = format_and_validate_input(numbers)

    # Decomposes the numbers into their individual digits
    for pns in formatted:
        # Add each digit to the total sum
        total += int(pns)

    return total

def sum_timestamp_digits():
    """Return the sum of digits in the current Unix timestamp."""
    # Get the current timestamp in seconds
    timestamp = str(time()).split('.')[0]

    return sum_all_digits(timestamp)

def lookup_for_digit(digit, numbers):
    """Check whether a digit exists in the input."""
    # Format and validate the input numbers
    formatted = format_and_validate_input(numbers)

    # Check if the digit is present in the numbers
    return str(digit) in str(formatted)

def count_digit_occurrences(digit, numbers):
    """Count the occurrences of a digit in the input."""
    # Format and validate the input numbers
    formatted = format_and_validate_input(numbers)

    # Count the occurrences of the digit in the numbers
    return str(formatted).count(str(digit))
