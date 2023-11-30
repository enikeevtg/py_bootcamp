import purse as p

def split_booty(*purses):
  # lst = []
  # for purse_ in purses:
  #   lst.append(purse_["gold_ingots"])
  # print(lst)
  purse_0 = p.get_ingot(purses[0])
  purse_1 = p.get_ingot(purses[0])
  purse_2 = p.get_ingot(purse_1)
  return (purse_0, purse_1, purse_2)

if __name__ == "__main__":
  print(split_booty(p.empty({}),
                    p.add_ingot(p.empty({})),
                    p.add_ingot(p.add_ingot(p.empty({})))
                    )
        )

  print(split_booty({"gold_ingots": 3},
                    {"gold_ingots": 2},
                    {"gold_ingots": 10}
                    )
        )
