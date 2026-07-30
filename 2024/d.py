n = int(input())
pizzas = []
for i in range(n):
    w, h = map(int, input().split())
    w, h = min(w, h), max(w, h)
    pizzas.append((w, h))
pizzas.sort(key=lambda x: x[1], reverse=True)

MAX = 1000000000
square = 0
minh = MAX
width = 0
for w, h in pizzas:
    minh = min(minh, h)
    width = min(MAX, width + w)
    square = max(square, min(minh, width))
print(square)