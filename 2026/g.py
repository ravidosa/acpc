n = int(input())
grid = []

def sqr(x, y):
    return x ** 2 + y ** 2

dicc = {}
for x in range(n // 2 + 1):
    for y in range(n // 2 + 1):
        r2 = sqr(x, y)
        dicc[r2] = 0

for i in range(n):
    line = input()
    for j in range(len(line)):
        if line[j] == "#":
            x, y = i - n // 2, j - n // 2
            p = [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
            sqrp = [sqr(pp[0], pp[1]) for pp in p]
            minsq, maxsq = min(sqrp), max(sqrp)
            for r2 in dicc.keys():
                if minsq <= r2 < maxsq:
                    dicc[r2] += 1

r, grass = 500 * 2, 0
for r2 in dicc.keys():
    if dicc[r2] > grass:
        grass = dicc[r2]
        r = r2 ** 0.5
    if dicc[r2] == grass:
        r = min(r, r2 ** 0.5)
print(dicc)
print(r)