# *args
def add(*nums):
  sum = 0
  for n in nums:
    sum += n
  return sum

print(add(1, 2, 3, 4, 5))

# **kwargs
def intro(**data):
    print("\nData type of argument: ", type(data))
    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
