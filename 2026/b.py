import math
n = int(input())
p = [int(i) for i in input().split()]
p.sort()

l = n // 2
u = n // 2 if n % 2 == 0 else n // 2 + 1
print(sum(p[u:]) - sum(p[:l]))