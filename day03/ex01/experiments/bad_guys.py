import argparse


parser = argparse.ArgumentParser(description='My example explanation')
parser.add_argument(
    '-e',
    type=str,
    default="1111111111,2222222222",
    help="provide a list of bad guys\' account numbers\
         (default: 1111111111,2222222222)"
)
bad_guys = parser.parse_args()
bad_guys_list = bad_guys.e.split(',')
print(bad_guys_list)
