
>>> # Problem 1
>>> def permutations(n, prefix = []):
    def generator(n, prefix = []):
        if len(prefix) == n:
            yield tuple(prefix)
        else:
            s = set(prefix)
            for i in range(1, n + 1):
                if i not in s:
                    yield from generator(n, prefix + [i])
    return list(generator(n))

>>> 
>>> # Problem 2
>>> def corr_bracket_seq(n):
    ps = set(['(' * n + ')' * n])
    for i in range(1, n):
        for a in corr_bracket_seq(i):
            for b in corr_bracket_seq(n-i):
                ps.add(a + b)
    return ps

>>> 
>>> # Problem 3
>>> def comb_repeats(n, k):
    def generator(n, k, prefix = []):
        if len(prefix) == k:
            yield tuple(prefix)
        else:
            m = max(prefix) if len(prefix) > 0 else 1
            for i in range(m, n + 1):
                yield from generator(n, k, prefix + [i])
    return list(generator(n, k))

>>> 
>>> # Problem 4
>>> def unord_part(n):
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

>>> 
