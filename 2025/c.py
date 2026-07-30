t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    suitless = map(int, input().split())
    numless = input().split()

    nummap = {i: 0 for i in range(1, 14)}
    suitmap = {s: 0 for s in "HSDC"}

    for s in suitless:
        nummap[s] += 1

    if any(map(lambda i: i > 4, nummap.values())):
        print("NO")
        continue

    for n in numless:
        suitmap[n] += 1
    
    if any(map(lambda i: i > 13, suitmap.values())):
        print("NO")
        continue
    
    for n in range(1, 14):
        for s in sorted("HSDC", key=lambda i: suitmap[i])[:nummap[n]]:
            suitmap[s] += 1
    
    if any(map(lambda i: i > 13, suitmap.values())):
        print("NO")
    else:
        print("YES")
