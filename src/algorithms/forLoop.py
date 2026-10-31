from time import time

def sum_all_digits(numbers):
    total = 0

    for n in numbers:
        for pns in str(n):
            total += int(pns)

    return total

def sum_timestamp_digits():
    # Get the current timestamp in seconds
    timestamp = str(time()).split('.')[0]

    return sum_all_digits(timestamp)

def lookup_for_digit(digit, numbers):
    for n in str(numbers):
        if str(digit) in str(n):
            return True

    return False

def count_digit_occurrences(digit, numbers):
    count = 0

    for n in str(numbers):
        if str(digit) in str(n):
            count += 1

    return count
