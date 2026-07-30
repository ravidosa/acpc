from functools import cache

n, k = map(int, input().split())

@cache
def fib(i):
    if i == 0 or i == 1:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)

if n <= 2:
    print("YES")
else:
    exp_a = fib(n - 3)
    exp_b = fib(n - 2)
    serve = True
    for i in range(k):
        p, q = map(int, input().split())
        serve = serve and ((q % exp_a == 0) or (q % exp_b == 0))
    print("YES" if serve else "NO")