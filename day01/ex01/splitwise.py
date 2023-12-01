import purse as p
import typing as t


def split_booty(*purses: t.Tuple[t.Dict[str, int]]):
    ingots_sum = 0
    purses_count = 3
    lst = []
    for purse in purses:
        ingots_sum += purse.get("gold_ingots", 0)
    for i in range(ingots_sum % purses_count):
        lst.append({'gold_ingots': ingots_sum // purses_count + 1})
    for i in range(ingots_sum % purses_count, purses_count):
        lst.append({'gold_ingots': ingots_sum // purses_count})
    return tuple(lst)
