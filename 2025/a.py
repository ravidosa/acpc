w, h, k = map(int, input().split())
w, h = min(w, h), max(w, h)

x = min(h - w, k)
x += (k - x) // 2
print((w + x) * (h + k - x))