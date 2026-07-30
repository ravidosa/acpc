import math

n = int(input())
ret = [n] + [int(i) for i in input().split()]

MOD = 10 ** 9 + 7

fact = [None] * (n + 1)
fact[0] = 1
for i in range(1, n + 1):
    fact[i] = (i * fact[i - 1]) % MOD

numerator = 1
denominator = 1
rem = n

for i in range(1, math.floor(n / 2) + 1):
    if rem == 0:
        break
    for j in range(1, math.floor(math.sqrt(i)) + 1):
        if i % j == 0:
            ret[i] -= ret[j] * (j != i) + ret[i // j] * (j != 1 and j * j != i)
    if ret[i] != 0:
        d = ret[i] // i
        num = (fact[rem] * pow(fact[i - 1], d, MOD)) % MOD
        denom = (((pow(fact[i], d, MOD) * fact[rem - ret[i]]) % MOD) * fact[d]) % MOD
        numerator = (numerator * num) % MOD
        denominator = (denominator * denom) % MOD
        rem -= ret[i]

if rem != 0:
    num = (fact[rem] * fact[rem - 1]) % MOD
    denom = fact[rem] % MOD
    numerator = (numerator * num) % MOD
    denominator = (denominator * denom) % MOD

print((numerator * pow(denominator, -1, MOD)) % MOD)