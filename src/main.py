import argparse

from algorithms import basicMath

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--digits", nargs="+", type=int, help="The digit to look up or count occurrences of.")
parser.add_argument("-c", "--count", type=int, help="Count occurrences of the digit.")
parser.add_argument("-l", "--lookup", type=int, help="Lookup a digit.")
parser.add_argument("-s", "--sum", action="store_true", help="Sum all digits in the input.")
parser.add_argument("-st", "--sum-timestamp", action="store_true", help="Sum digits in the current timestamp.")

args = parser.parse_args()

def require_digits(function):
    if not args.digits:
        print(f"\033[31mError: The {function} option requires the --digits option.\033[0m")
        exit(1)

options_in_use = sum((
    args.count is not None,
    args.lookup is not None,
    args.sum,
    args.sum_timestamp
))

match True:
    # Only one type of operation is permitted at the time
    case _ if options_in_use > 1:
        print("\033[31mError: Cannot use both --count, --lookup, --sum and --sum-timestamp options together.\033[0m")
        exit(1)
    # Lookup a digit
    case _ if args.lookup is not None:
        require_digits("--lookup")
        value = basicMath.lookup_for_digit(args.lookup, args.digits)
        print(f"\033[34mValue of digit {args.digits}: \033[33m{value}\033[0m")
    # Count occurrences of the digit in the input
    case _ if args.count is not None:
        require_digits("--count")
        value = basicMath.count_digit_occurrences(args.count, args.digits)
        print(f"\033[34mOccurrences of digit {args.digits}: \033[33m{value}\033[0m")
    # Sum of all digits parsed
    case _ if args.sum:

        require_digits("--sum")
        print(f"\033[34mSum of all digits: \033[33m{basicMath.sum_all_digits(args.digits)}\033[0m")
    # Sum digits in the current timestamp
    case _ if args.sum_timestamp:
        print(f"\033[34mSum of timestamp digits: \033[33m{basicMath.sum_timestamp_digits()}\033[0m")
    # The default use case
    case _:
        print("\033[31mError: No valid option provided.\033[0m")
