# Exercise 02: Track and Capture
# Code prints 'True' if M-pattern exists in a given
# input text-image or 'False' otherwise
import sys


m_refereced_lines = ["*   *",
                     "** **",
                     "* * *"]


def ContentChecking(content):
    if len(content) != 3:
        return False
    for line in content:
        line = line.strip()
        if len(line) != 5:
            return False
    return True


def isContainM(content):
    for i in range(3):
        line = content[i].strip()
        filtered_line = ""
        for j in range(5):
            if line[j] != '*':
                filtered_line = filtered_line + ' '
            else:
                filtered_line = filtered_line + '*'
        if filtered_line != m_refereced_lines[i]:
            return "False"
    return "True"


params_count = len(sys.argv)
if params_count != 2:
    print("one parameter expected")
else:
    f = open(sys.argv[1], "r")
    content = f.readlines()
    if ContentChecking(content) is False:
        print("Error")
    else:
        print(isContainM(content))
