class Key:
    passphrase = str(None)

    # __magic_methods__:
    def __init__(self, passphrase_="zax2rulez"):
        self.passphrase = passphrase_

    def __len__(self) -> int:
        return 1337

    def __getitem__(self, key) -> int:
        return 3

    # greater than
    def __gt__(self, other) -> bool:
        return 9999 > other

    def __str__(self) -> str:
        return "GeneralTsoKeycard"
