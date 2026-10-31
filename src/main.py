from algorithms import forLoop

print("- sum_all_digits:")

# Sum all digits to get 30, using a list
sum_to_30 = forLoop.sum_all_digits([1, 2, 3, 4, 5, 6, 7, 11])
print("list: 30 = " + str(sum_to_30))
try:
    sum_to_30 = forLoop.sum_all_digits([1, 2, 3, 4, 5, 6, 7, 11, "abc"])
except ValueError as e:
    print("Error using list: " + str(e))

# Sum all digits to get 30, using set
sum_to_30 = forLoop.sum_all_digits({1, 2, 3, 4, 5, 6, 7, 11})
print("set: 30 = " + str(sum_to_30))
try:
    sum_to_30 = forLoop.sum_all_digits({1, 2, 3, 4, 5, 6, 7, 11, "abc"})
except ValueError as e:
    print("Error using set: " + str(e))

# Sum all digits to get 30, using a tuple
sum_to_30 = forLoop.sum_all_digits((1, 2, 3, 4, 5, 6, 7, 11))
print("tuple: 30 = " + str(sum_to_30))
try:
    sum_to_30 = forLoop.sum_all_digits((1, 2, 3, 4, 5, 6, 7, 11, "abc"))
except ValueError as e:
    print("Error using tuple: " + str(e))

# Sum all digits to get 30, using a number
sum_to_30 = forLoop.sum_all_digits(123456711)
print("number: 30 = " + str(sum_to_30))

# Sum all digits to get 30, using a string
sum_to_30 = forLoop.sum_all_digits("123456711")
print("string: 30 = " + str(sum_to_30))
try:
    sum_to_30 = forLoop.sum_all_digits("123456711abc")
except ValueError as e:
    print("Error using string: " + str(e))

print("\n")
print("- sum_timestamp_digits:")

# Sum all digits of the current timestamp
print(forLoop.sum_timestamp_digits())

print("\n")
print("- lookup_for_digit:")

# Lookup for digit in a list of numbers
print(forLoop.lookup_for_digit(3, [1, 2, 3, 4, 5]))  # True
print(forLoop.lookup_for_digit(6, [1, 2, 3, 4, 5]))  # False
print(forLoop.lookup_for_digit(1, 102030))  # True
print(forLoop.lookup_for_digit(6, 102030))  # False
print(forLoop.lookup_for_digit(1, "102030"))  # True
print(forLoop.lookup_for_digit(6, "102030"))  # False

print("\n")
print("- count_digit_occurrences:")

# Lookup for digit in a list of numbers and count occurrences
print(forLoop.count_digit_occurrences(3, [1, 2, 3, 4, 5]))  # 1
print(forLoop.count_digit_occurrences(6, [1, 2, 3, 4, 5]))  # 0
print(forLoop.count_digit_occurrences(0, 102030))  # 3
print(forLoop.count_digit_occurrences(6, 102030))  # 0
print(forLoop.count_digit_occurrences(0, "102030"))  # 3
print(forLoop.count_digit_occurrences(6, "102030"))  # 0

print(str([1, 2, 3, 4, 5]))