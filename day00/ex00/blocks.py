# Exercise 00: Blockchain
# Hashes checking:
# - Correct lines are 32 characters long
# - They start with exactly 5 zeroes, so e.g. line starting with 6 zeroes is NOT
# considered correct

import sys

params_count = len(sys.argv)
if (params_count != 2):
  print("one parameter expected")
else:
  param = str(sys.argv[1])
  if (param.isdigit() == False):
    print(f"parameter \"{param}\" is not valid")
  else:
    start_of_hash = "00000"
    hashes_count = int(param)
    for i in range(hashes_count):
      hash = input()
      if (len(hash) == 32 and
          hash[:5] == start_of_hash and
          hash[5] != '0'):
        print(hash)
