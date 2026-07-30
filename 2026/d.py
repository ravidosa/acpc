t = int(input())
for _ in range(t):
    n = int(input())
    v = [int(i) for i in input().split()]
    res = 0
    prefix_forward = v.copy()
    prefix_backward = v.copy()
    for i in range(1, n):
        prefix_forward[i] += prefix_forward[i-1]
        prefix_backward[-i-1] += prefix_backward[-i]
    for i in range(1, n):
        res = max(res, (n - i) * prefix_forward[i-1] - i * prefix_backward[i])
    print(res)