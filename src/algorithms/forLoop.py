from time import time

def sum_all_digits(numbers):
    total = 0

    # Ensure that the input is converted to a string
    formatted = "".join(str(n) for n in numbers)

    # Validate that the input contains only numeric digits
    if not formatted.isdigit():
        raise ValueError("Input contains non-numeric characters")

    # Decomposes the numbers into their individual digits
    for pns in formatted:
        # Add each digit to the total sum
        total += int(pns)

    return total

def sum_timestamp_digits():
    # Get the current timestamp in seconds
    timestamp = str(time()).split('.')[0]

    return sum_all_digits(timestamp)

def lookup_for_digit(digit, numbers):
    # Check if the digit is present in the numbers
    return str(digit) in str(numbers)

def count_digit_occurrences(digit, numbers):
    # Count the occurrences of the digit in the numbers
    return str(numbers).count(str(digit))
