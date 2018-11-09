# Problem 1
def permutations(n, prefix = []):
    def generator(n, prefix = []):
        if len(prefix) == n:
            yield tuple(prefix)
        else:
            s = set(prefix)
            for i in range(1, n + 1):
                if i not in s:
                    yield from generator(n, prefix + [i])
    return list(generator(n))


# Problem 2
def correctbracketsequences(n):
    def generator(n, prefix = '', balance = 0):
        if len(prefix) == 2 * n and balance == 0:
            yield prefix
        else:
            for i in ('(', ')'):
                new_prefix = prefix + i
                new_balance = balance + (1 if i == '(' else -1)
                if len(new_prefix) <= 2 * n and new_balance >= 0:
                    yield from generator(n, new_prefix, new_balance)
    return list(generator(n))


# Problem 3
def combinationswithrepeats(n, k):
    def generator(n, k, prefix = []):
        if len(prefix) == k:
            yield tuple(prefix)
        else:
            m = max(prefix) if len(prefix) > 0 else 1
            for i in range(m, n + 1):
                yield from generator(n, k, prefix + [i])
    return list(generator(n, k))


# Problem 4
def unorderedpartitions(n):
    def generator(n, prefix = []):
        if sum(prefix) == n:
            yield tuple(prefix)
        else:
            m = prefix[-1] if len(prefix) > 0 else 1
            for i in range(m, n - m + 2):
                new_prefix = prefix + [i]
                if sum(new_prefix) <= n:
                    yield from generator(n, prefix + [i])
    return list(generator(n))

    #hello buddy!
