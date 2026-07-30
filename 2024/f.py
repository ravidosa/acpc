from functools import cache

b = input()
d = input()
n, m, MOD = len(b), len(d), 10 ** 9 + 7

@cache
def rem(pb, pd, can_rem):
    if pd == m:
        return pb >= n - can_rem
    elif pb == n:
        return 0
    res = 0
    if can_rem:
        res += rem(pb + 1, pd, 0)
    if b[pb] == d[pd]:
        res += rem(pb + 1, pd + 1, 1)
    return res % MOD

print(rem(0, 0, 1))