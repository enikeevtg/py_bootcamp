import argparse


parser = argparse.ArgumentParser(description="Sum of numbers")
parser.add_argument("first_number", type=int, help="Input first number")
parser.add_argument("second_number", type=int, help="Input second number")
args = parser.parse_args()
print(args.first_number + args.second_number)
