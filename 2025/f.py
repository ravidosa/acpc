d, p, h = map(int, input().split())
sat = [0] + [int(i) for i in input().split()]

children = {}
has_parent = [False] * (d + 1)
for _ in range(p):
    a, b = map(int, input().split())
    children[a] = children.get(a, []) + [b]
    has_parent[b] = True
roots = [i for i in range(1, d + 1) if not has_parent[i]]

paths = {0: 0}
for root in roots:
    stack = [(root, sat[root], 1)]
    while stack:
        node, curr_sum, curr_len = stack.pop()
        paths[curr_sum] = min(paths.get(curr_sum, float("inf")), curr_len)
        for child in children.get(node, []):
            stack.append((child, curr_sum + sat[child], curr_len + 1))
sats = sorted(paths.keys())

hunger = [int(i) for i in input().split()]
for hung in hunger:
    lo, hi = 0, len(sats) - 1
    pos = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sats[mid] <= hung:
            pos = mid
            lo = mid + 1
        else:
            hi = mid - 1
    if pos < 0:
        print("0 0")
    else:
        print(f"{sats[pos]} {paths[sats[pos]]}")