from argparse import ArgumentParser
from redis import Redis
import json
import random

min_account: int = 1e9
max_account: int = 1e10 - 1
min_amount: int = -1e5
max_amount: int = 1e5

mess_1 = {"metadata": {"from": 1111111111, "to": 2222222222}, "amount": 10000}
mess_2 = {"metadata": {"from": 3333333333, "to": 4444444444}, "amount": -3000}
mess_3 = {"metadata": {"from": 2222222222, "to": 5555555555}, "amount": 5000}

hostname = "localhost"
port = 6379
db = 0
channel_name = "channel"

default_bad_guys = "2222222222,4444444444"
