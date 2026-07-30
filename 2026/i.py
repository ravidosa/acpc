import math
n, c, t = map(int, input().split())

runs = t // c
if runs == 0:
    print(-1)
else:
    logg = math.ceil(math.log(n))

    for m in range(1, logg + 1):
        if m < runs:
            if sum(1, m + 1) >= logg:
                break
        else:
            if (m + (m - runs + 1)) * runs // 2 >= logg:
                break
    print(m)