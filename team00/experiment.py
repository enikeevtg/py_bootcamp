from bs4 import BeautifulSoup
import json

current_depth = 1
max_depth = 3

# script scheme:
def recurs(link, current_depth) -> dict:
    # page reading:
    soup = BeautifulSoup(link, "html.parser")

    # result: 
    lst = [
      "link1",
      "link2",
      "link3"
    ]

    dct = {}
    if current_depth < max_depth:
        for key in lst:
            dct[str(key)] = recurs(key, current_depth + 1)

    return dct


# data = {
#   "page1": {"page2": 1, "page3": 1},
#   "page2": [1, 5, 7],
#   "page3": [1, 9, 2]
# }

# with open("./experiment.json", "w") as fp:
#     fp.write(json.dumps(data))

with open("./experiment.json", "r") as fp:
    content = fp.read()
    # print(json.loads(content))
    with open("./experiment1.json", "w") as fp:
        fp.write(json.dumps(json.loads(content), indent=2))
