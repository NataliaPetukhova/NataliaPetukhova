# Problem 1
def valuesunion(*dicts):
    return set().union(chain.from_iterable([x.values() for x in dicts]))


# Problem 2
def subpalindrome1(s):
    rev = s[::-1]
    l = len(s)
    while l > 0:
        for i in range(0, len(s) - l + 1):
            half = int(l / 2)
            left = s[i: i + half]
            right = rev[len(s) - (i + l): len(s) - (i + l - half)]
            if left == right:
                return s[i:i + l]
        l -= 1
    return None


# Problem 3
def powers(n, m):
    return dict([(i, i ** (i % m)) for i in range(1, n + 1)])


# Problem 4
def popcount(n):
    count = 0
    while n > 0:
        count += 1
        n &= n - 1
    return count


# Problem 5
def isipv4(ip):
    return re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip) != None


# Problem 6
from functools import reduce
fib=lambda n:reduce(lambda x,y:(x[0]+x[1],x[0]),[(1,1)]*(n-2))[0]


