import crack


def assertion_test():
    key = crack.Key()
    assert len(key) == 1337
    assert key[404] == 3
    assert key > 9000
    assert key.passphrase == "zax2rulez"
    assert str(key) == "GeneralTsoKeycard"
    print("Assertion: len(key) == 1337 is", len(key) == 1337)
    print("Assertion: key[404] == 3 is", key[404] == 3)
    print("Assertion: key > 9000 is", key > 9000)
    print(
        'Assertion: key.passphrase == "zax2rulez" is',
        key.passphrase == "zax2rulez"
    )
    print(
        'Assertion: str(key) == "GeneralTsoKeycard" is',
        str(key) == "GeneralTsoKeycard"
    )


if __name__ == "__main__":
    assertion_test()
