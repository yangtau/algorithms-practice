'''
KMP Algorithm: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
'''


def kmp_table(t) -> [int]:
    table = [-1] * len(t)
    pos = 1  # the current postion we are computing in T
    cnd = 0  # the index of the next char of the current candidate substring

    while pos < len(t):
        if t[pos] == t[cnd]:
            table[pos] = table[cnd]
        else:
            table[pos] = cnd
            while cnd >= 0 and t[cnd] != t[pos]:
                cnd = table[cnd]
        pos += 1
        cnd += 1

    table.append(cnd)  # need when all word occurrences searched
    return table


def kmp(s, t):
    '''return the lowerest index in `s` where substring `t` is found'''
    if len(s) < len(t):
        return -1
    if len(t) == 0:
        return 0
    table = kmp_table(t)
    idx = 0  # the index of current char in t
    for pos in range(len(s)):
        if s[pos] == t[idx]:
            if idx == len(t) - 1:
                return pos - idx
        else:
            idx = table[idx]
            while idx >= 0 and s[pos] != t[idx]:
                idx = table[idx]
        idx += 1
    return -1
