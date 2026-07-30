b = input()
n = int(input())
for i in range(n):
    d = input()
    pb, pd = 0, 0
    while pb < len(b) and pd < len(d):
        if b[pb] == d[pd]:
            pb += 1
            pd += 1
        else:
            pb += 1
    print("YES" if pd == len(d) else "NO")
