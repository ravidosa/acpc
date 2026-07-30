from itertools import combinations

n = int(input())
gx, gy = map(int, input().split())
g = (gx, gy)
p = []
for i in range(n):
    px, py = map(int, input().split())
    p.append((px, py))

def area(p1, p2, p3):
    return 0.5 * abs(p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[1]*p2[0] - p2[1]*p3[0] - p3[1]*p1[0])

def inside(p1, p2, p3, p):
    denominator = ((p2[1] - p3[1]) * (p1[0] - p3[0]) +
                   (p3[0] - p2[0]) * (p1[1] - p3[1]))
    a = ((p2[1] - p3[1]) * (p[0] - p3[0]) +
         (p3[0] - p2[0]) * (p[1] - p3[1])) / denominator
    b = ((p3[1] - p1[1]) * (p[0] - p3[0]) +
         (p1[0] - p3[0]) * (p[1] - p3[1])) / denominator
    c = 1 - a - b
    return (a >= 0 and b >= 0 and c >= 0)

res = 0
for comb in combinations(p, 3):
    p1, p2, p3 = comb
    if inside(p1, p2, p3, g):
        res = max(res, area(p1, p2, p3))
print(-1 if res == 0 else res)