import typing as t


def alarm_decorator(func):
    def wrapper(purse):
        print("SQUEAK")
        return func(purse)
    return wrapper


@alarm_decorator
def empty(purse: t.Dict[str, int]):
    return {}


@alarm_decorator
def add_ingot(purse: t.Dict[str, int]):
    purse_copy = purse.copy()
    new_ingots_count = purse.get('gold_ingots', 0) + 1
    purse_copy['gold_ingots'] = new_ingots_count
    return purse_copy


@alarm_decorator
def get_ingot(purse: t.Dict[str, int]):
    purse_copy = purse.copy()
    if purse.get('gold_ingots', False) is not False:
        purse_copy["gold_ingots"] = purse.get('gold_ingots') - 1
        if purse_copy["gold_ingots"] == 0:
            purse_copy.pop('gold_ingots')
    return purse_copy
