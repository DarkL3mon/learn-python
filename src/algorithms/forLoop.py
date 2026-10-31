from time import time

def sum_all_digits(numbers):
    total = 0

    for n in numbers:
        if n > 9:
            # Split the number into its individual digits
            parts = list(str(n))

            # Parse each digit back to an integer and sum them up
            total += sum_all_digits([int(p) for p in parts])
        else:
            total += n

    return total

def sum_timestamp_digits():
    # Get the current timestamp in seconds
    timestamp = str(time()).split('.')[0]

    return sum_all_digits([int(digit) for digit in timestamp])
