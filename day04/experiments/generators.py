# next
def test(n: int):
    for i in range(n):
        yield i


def test_oneline(n: int):
    yield from [i for i in range(n)]


for i in test_oneline(11):
    print(i, end=" ")
print()


# iter
a = iter("test")
for c in a:
    print(c)

for c in a:
    print(c)


# some yield
def test2():
    while True:
        yield True
        yield False


a = test2()
for i in range(11):
    print(next(a))


# send
def test_send():
    while True:
        a = yield
        print("a.send(", a, ")")


a = test_send()
next(a)
for i in test(5):
    a.send(i)
