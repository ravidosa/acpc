n = int(input())
s = [int(i) for i in input().split()]

ch = [None] * n

for i in range(n - 1, -1, -1):
    if i == n - 1:
        ch[i] = "d"
    elif ch[i + 1] == "x":
        ch[i] = "d"
    elif i + s[i] + 1 < n and ch[i + s[i] + 1] == "x":
        ch[i] = "c"
    elif i + s[i] == n - 1:
        ch[i] = "c"
    else:
        ch[i] = "x"

if ch[0] == "x":
    print("NO")
else:
    print("YES")