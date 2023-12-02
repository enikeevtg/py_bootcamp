# Exercise 01: Decypher
import sys


params_count = len(sys.argv)
if params_count < 2:
    print("some parameters expected")
else:
    code = sys.argv[1]
    decode = ""
    for word in code.split(" "):
        decode += word[0]
    print(decode)


# https://github.com/maybeIllchangeitlater/school21projects/blob/main/PythonBootcamp/Day00/decypher.py
# import sys

# def decipher(input_str: list[str]):
#     answer = ""
#     for s in input_str[1:]:
#       for s1 in s.split(' '):
#         answer += s1[0]
#     print(answer)


# def main():
#     input_strings = sys.argv
#     decipher(input_strings)


# if __name__ == "__main__":
#     main()
