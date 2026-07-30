n = int(input())
h = [0] + [int(i) for i in input().split()]

print(max([abs(h[i] - h[i - 1]) for i in range(1, n + 1)]))