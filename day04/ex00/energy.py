import itertools
import unittest


def fix_wiring(c: list, s: list, p: list) -> list:
    return ([f"plug {wiring[0]} into {wiring[1]} using {wiring[2]}"
            for wiring in zip(
                [c_ for c_ in c if type(c_) is str],
                [s_ for s_ in s if type(s_) is str],
                [p_ for p_ in p if type(p_) is str])] +
            [f"weld {wiring[0]} to {wiring[1]} without plug"
            for wiring in itertools.zip_longest(
                [c_ for c_ in c if type(c_) is str],
                [s_ for s_ in s if type(s_) is str],
                [p_ for p_ in p if type(p_) is str]) if wiring[0] and wiring[1]
                and wiring[2] is None])


class Test(unittest.TestCase):
    def test_1(self):
        print("test_1")
        plugs = ['plug1', 'plug2', 'plug3']
        sockets = ['socket1', 'socket2', 'socket3', 'socket4']
        cables = ['cable1', 'cable2', 'cable3', 'cable4']

        reference_list = ["plug cable1 into socket1 using plug1",
                          "plug cable2 into socket2 using plug2",
                          "plug cable3 into socket3 using plug3",
                          "weld cable4 to socket4 without plug"]
        i = 0
        for c in fix_wiring(cables, sockets, plugs):
            self.assertEqual(reference_list[i], c)
            i += 1

    def test_2(self):
        print("\ntest_2")
        plugs = ['plugZ', None, 'plugY', 'plugX']
        sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
        cables = ['cable2', 'cable1', False]

        reference_list = ["plug cable2 into socket1 using plugZ",
                          "plug cable1 into socket2 using plugY"]
        i = 0
        for c in fix_wiring(cables, sockets, plugs):
            self.assertEqual(reference_list[i], c)
            i += 1


if __name__ == "__main__":
    unittest.main()
