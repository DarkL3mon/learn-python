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
