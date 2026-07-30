from math import sqrt

a, b = map(int, input().split())
a, b = min(a, b), max(a, b)

if b / (2 * sqrt(3)) >= a * sqrt(3) / 2:
    print(b / sqrt(3))
else:
    print(0.5 * (a + b) * sqrt(3) / 2)