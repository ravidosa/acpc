n = int(input())
s = []
for i in range(n):
    s.append(input())
m = int(input())
ans = 0
for i in range(m):
    t = input()
    for head in s:
        repl = "G" + head[1:]
        if repl == t:
            ans += 1
            break
print(ans)