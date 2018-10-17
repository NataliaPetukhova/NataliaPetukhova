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
        print("yes")
    else:
        return recurrent((n-1) // 2 + 1) + recurrent((n-1) // 2)


# Problem 4
def digitsum(n) :
    sum = 0
    while (n != 0) : 
        sum = sum + n % 10
        n = n// 10 
    return sum


# Problem 5
def reversestring(s):
    return s[::-1]


# Problem 6
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ack(m, n - 1))


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
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2
        return True


# Problem 10
def concatnumbers(a, b):
    return a * (10 ** len(str(b))) + b


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

















