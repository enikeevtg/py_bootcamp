def empty(purse):
  return dict(gold_ingots = 0)

def add_ingot(purse):
  if len(purse) > 0:
    new_ingots_count = purse['gold_ingots'] + 1
  else:
    new_ingots_count = 0
  return dict(gold_ingots = new_ingots_count)

def get_ingot(purse):
  if len(purse) > 0:
    new_ingots_count = purse['gold_ingots']
    if new_ingots_count > 0:
      new_ingots_count -= 1
  else:
    new_ingots_count = 0
  return dict(gold_ingots = new_ingots_count)

if __name__ == "__main__":
  purse = {}
  print("purse = {}:", purse)
  purse = empty(purse)
  print("purse = empty(purse):", purse)
  purse = add_ingot(purse)
  print("purse = add_ingot(purse):", purse)
  purse = get_ingot(purse)
  print("purse = get_ingot(purse):", purse)
  print("add_ingot(get_ingot(add_ingot(empty(purse))))", end = " == ")
  print("{'gold_ingots': 1}", end = " is ")
  print(add_ingot(get_ingot(add_ingot(empty(purse)))) == {'gold_ingots': 1})
 