import itertools
from functools import reduce

# Problem1
def squares(a):
    for i in a:
        yield i**2


# Problem2
def repeatntimes(elems, n):
    it = itertools.tee(elems, n)
    for i in it:
        yield from i


# Problem3
def evens(x):
    if x % 2:
        x = +1
    while True:
        x += 2
        yield x


# Problem4
def digitsumdiv(p):
    for i in itertools.count(1):
        if not sum(map(int, str(i))) % p:
            yield i


# Problem5
def extractnumbers(s):
    return filter(lambda x: x.isdigit(), s)


# Problem6
def changecase(s):
        return map(lambda x: x.swapcase() if x.isalpha() else x, s)


# Problem7
def productif(elem, cond):
    return reduce(lambda x, y: x * y, map(lambda x: x[0] if x[1] else 1,
zip(elem, cond)), 1)






