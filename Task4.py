# Problem 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


# Problem 2
def fibonacci(n):
    if n < 3:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


# Problem 3
def recurrent(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return recurrent(n // 2)
    else:
        return recurrent((n-1) // 2 + 1) + recurrent((n-1) // 2)


# Problem 4
def digitsum(n) :
    if n // 10 == 0:
        return n
    else:
        return n % 10 + digitsum(n // 10)


# Problem 5
def reversestring(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reversestring(s[0:-1])

# Problem 6
def ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m-1, ackermann(m, n - 1))


# Problem 7
def drawborders(n):
    if n == 1:
        return ['+']
    elif n == 2:
        return ['++',
                '++']
    else:
        answ = [0 for x in range(n)]
        answ[0] = '+'
        for i in range(n - 2):
            answ[0] += '-'
        answ[0] += '+'
        for i in range(1, n - 1):
            answ[i] = '|' + drawborders(n - 2)[i - 1] + '|'
        answ[n - 1] = '+'
        for i in range(n - 2):
            answ[n - 1] += '-'
        answ[n - 1] += '+'
        return answ

# Problem 8
def genbinarystrings(n):
  if n == 0:
    return ['']
  small = genbinarystrings(n-1)
  lst = []
  for item in small:
    lst.append(item + '0')
    lst.append(item + '1')
  return lst


# Problem 9
def istwopower(n):
    if n == 1:
        return True
    elif n <= 0:
        return False
    elif n % 2 == 0:
        return istwopower(n // 2)
    return False


# Problem 10
def concatnumbers(a, b):
   if b // 10 == 0:
        return a*10 + b
    else:
        return concatnumbers(a * 10 + b // (10 ** (len(str(b)) - 1)),
                             b % (10 ** (len(str(b)) - 1)))


# Problem 11
def abacaba(n):
    if n == 1:
        return [1]
    else:
        return abacaba(n - 1) + [n] + abacaba(n - 1)


# Problem 12
def parentheses(s):
    if len(s) in {0, 1, 2}:
        return "(" + s + ")"
    else:
        return "(" + s[0] + parentheses(s[1:-1]) + s[-1] + ")"


# Problem 13
def gcd(a, b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)


# Problem 14
def mergesort(a):
    result = []
    if len(a) < 2:
        return a
    mid = int(len(a) / 2)
    x = mergesort(a[:mid])
    y = mergesort(a[mid:])
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] > y[j]:
            result.append(y[j])
            j += 1
        else:
            result.append(x[i])
            i += 1
    result += x[i:]
    result += y[j:]
    return result
























