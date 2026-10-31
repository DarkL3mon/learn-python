from algorithms import forLoop

# Sum all digits to get 30
sum_to_30 = forLoop.sum_all_digits([1, 2, 3, 4, 5, 6, 7, 11])
print("30 = " + str(sum_to_30))

# Sum all digits of the current timestamp
print(forLoop.sum_timestamp_digits())

# Lookup for digit in a list of numbers
print(forLoop.lookup_for_digit(3, [1, 2, 3, 4, 5]))  # True
print(forLoop.lookup_for_digit(6, [1, 2, 3, 4, 5]))  # False
print(forLoop.lookup_for_digit(1, 102030))  # True
print(forLoop.lookup_for_digit(6, 102030))  # False
print(forLoop.lookup_for_digit(1, "102030"))  # True
print(forLoop.lookup_for_digit(6, "102030"))  # False
