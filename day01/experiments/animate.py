import os
import time


def animain():
    string = str("")
    for i in range(11):
        time.sleep(1)
        os.system("clear")
        string += "#"
        print(string)


if __name__ == "__main__":
    animain()
