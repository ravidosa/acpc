from functools import cache
import math

n = int(input())
MOD = 10 ** 9 + 7

arr = [0] * (n + 1)
arr[0] = 2

for i in range(1, n + 1):
    j = 1
    while j <= i:
        arr[i] = (arr[i] + arr[i - j]) % MOD
        j *= 2


print(arr[n])