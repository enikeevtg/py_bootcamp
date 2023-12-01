import os
import purse as p
import splitwise as s


def test_split():
    print("********************")
    print("test_split():")
    purse0 = {'gold_ingots': 3}
    purse1 = {'gold_ingots': 2}
    purse2 = {'apples': 10}
    print("\tpurse0:", purse0)
    print("\tpurse1:", purse1)
    print("\tpurse2:", purse2)
    print("\tsplit_booty(purse0, purse1, purse2):\n\t",
          s.split_booty(purse0, purse1, purse2))
    print("\tpurse0:", purse0)
    print("\tpurse1:", purse1)
    print("\tpurse2:", purse2)


if __name__ == "__main__":
    os.system('clear')
    test_split()
