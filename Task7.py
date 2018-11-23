import functools
import itertools


# Problem 1
def valuesunion(*dicts):
    ans = set()
    for d in dicts:
        for el in d.values():
            ans.add(el)
    return ans


# Problem 2
def subpalindrome(string):

    def check(word):
        if len(word) == 1:
            return True
        return all(word[i] == word[-1 * (i + 1)] for i in range(len(word) // 2))

    subpal = ''
    max = 0
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if check(string[i:j]):
                if j - i > max:
                    subpal = string[i:j]
                    max = j - i
                elif j - i == max:
                    if string[i:j] < subpal:
                        subpal = string[i:j]

    return subpal


# Problem 3
def powers(n, m):
    answ = {}

    def power(n):
        a = 1
        for i in range(n):
            a *= n
        return a

    for i in range(1, n+1):
        answ[i] = power(i) % m
    return answ


# Problem 4
def popcount(n):
    count = 0
    while n > 0:
        count += 1
        n &= n - 1
    return count


# Problem 5
def isIPv4(s):
    parts = s.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True


# Problem 6
def fibonacci(n):
    return functools.reduce(lambda x, n: [x[1], x[0] + x[1]], range(n), [0, 1])[0]


# Problem 7
def pascals():
    prev = (1,)

    for i in itertools.count(1):
        act = []
        act.append(1)
        for k in range(len(prev) - 1):
            act.append(prev[k] + prev[k + 1])
        act.append(1)
        yield tuple(prev)
        prev = act


