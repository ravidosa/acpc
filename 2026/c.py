import math
n, h = map(int, input().split())

def prob_c(n, h):
    lvl = 1
    while h // (2**lvl) >= 1:
        lvl += 1
    lvl -= 1

    ct = h * (n-lvl)
    while lvl >= 0:
        ct += 2 ** lvl
        lvl -= 1
    print(ct)

prob_c(n,h)