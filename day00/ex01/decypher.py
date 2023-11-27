# Exercise 01: Decypher

import sys

params_count = len(sys.argv)

if (params_count < 2):
  print("some parameters expected")
else:
  code = sys.argv[1]
  decode = ""
  for word in code.split(' '):
    decode = decode + word[0]
  print(decode)
