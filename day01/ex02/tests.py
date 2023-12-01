import os
import purse as p


def test_empty(purse):
    print("********************")
    print("test_empty(purse):")
    print("\tpurse:", purse)

    print("\tempty(purse):", p.empty(purse))
    print("\tpurse:", purse)

    purse = p.empty(purse)
    print("\tpurse = empty(purse):", purse)


def test_add(purse):
    print("********************")
    print("test_add(purse):")
    print("\tpurse:", purse)

    print("\tadd_ingot(purse):", p.add_ingot(purse))
    print("\tpurse:", purse)

    for i in range(3):
        purse = p.add_ingot(purse)
        print("\tpurse = add_ingot(purse):", purse)


def test_get(purse):
    print("********************")
    purse['gold_ingots'] = 3
    print("test_get(purse):")
    print("\tpurse:", purse)

    print("\tget_ingot(purse):", p.get_ingot(purse))
    print("\tpurse:", purse)

    for i in range(4):
        purse = p.get_ingot(purse)
        print("\tpurse = get_ingot(purse):", purse)


def test_complex(purse):
    print("********************")
    print("add_ingot(get_ingot(add_ingot(empty(purse))))", end=" == ")
    print("{'gold_ingots': 1}", end=" is ")
    print(
      p.add_ingot(p.get_ingot(p.add_ingot(p.empty(purse)))) is
      {'gold_ingots': 1}
      )


if __name__ == "__main__":
    os.system('clear')
    purse = {'coins': 11}
    test_empty(purse)
    test_add(purse)
    test_get(purse)
    # test_complex(purse)
