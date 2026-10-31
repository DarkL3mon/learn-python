from algorithms import forLoop

# Sum all digits to get 30
sum_to_30 = forLoop.sum_all_digits([1, 2, 3, 4, 5, 6, 7, 11])
print("30 = " + str(sum_to_30))

# Should raise ValueError for non-numeric characters
try:
    sum_to_30 = forLoop.sum_all_digits([1, 2, 3, 4, 5, 6, 7, 11, "abc"])
    print("30 = " + str(sum_to_30))
except ValueError as e:
    print("Error: " + str(e))

# Sum all digits of the current timestamp
print(forLoop.sum_timestamp_digits())

# Lookup for digit in a list of numbers
print(forLoop.lookup_for_digit(3, [1, 2, 3, 4, 5]))  # True
print(forLoop.lookup_for_digit(6, [1, 2, 3, 4, 5]))  # False
print(forLoop.lookup_for_digit(1, 102030))  # True
print(forLoop.lookup_for_digit(6, 102030))  # False
print(forLoop.lookup_for_digit(1, "102030"))  # True
print(forLoop.lookup_for_digit(6, "102030"))  # False

# Lookup for digit in a list of numbers and count occurrences
print(forLoop.count_digit_occurrences(3, [1, 2, 3, 4, 5]))  # 1
print(forLoop.count_digit_occurrences(6, [1, 2, 3, 4, 5]))  # 0
print(forLoop.count_digit_occurrences(0, 102030))  # 3
print(forLoop.count_digit_occurrences(6, 102030))  # 0
print(forLoop.count_digit_occurrences(0, "102030"))  # 3
print(forLoop.count_digit_occurrences(6, "102030"))  # 0

print(str([1, 2, 3, 4, 5]))