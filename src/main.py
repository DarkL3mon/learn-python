import argparse

from algorithms import basicMath

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--digits", nargs="+", type=int, help="The digit to look up or count occurrences of.")
parser.add_argument("-c", "--count", type=int, help="Count occurrences of the digit.")
parser.add_argument("-s", "--sum", action="store_true", help="Sum all digits in the input.")

args = parser.parse_args()

# Check for mutually exclusive options
if args.sum and args.count:
    print("\033[31mError: Cannot use both --sum and --count options together.\033[0m")
    exit(1)

if args.sum:
    # Sum all digits in the input
    print(f"\033[34mSum of all digits: \033[33m{basicMath.sum_all_digits(args.digits)}\033[0m")
elif args.count:
    # Count occurrences of the digit in the input
    value = basicMath.count_digit_occurrences(args.count, args.digits)
    print(f"\033[34mOccurrences of digit {args.digits}: \033[33m{value}\033[0m")
