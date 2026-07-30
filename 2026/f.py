ct = int(input())
jockeys = [int(i) for i in input().split()]
jockeys.sort()


def prob_f(jockeys):
    d = {}
    for jockey in jockeys:
        if jockey not in d:
            d[jockey] = 0
        else:
            d[jockey] += 1

    col = 1
    row = len(d.keys())
    row_spot = row-1//2
    tot_spot = row_spot

    keys = d.keys()
    for key in keys:
        if d[key] == 0:
            del d[key]

    while len(d.keys()):
        curr_row = len(d.keys())
        if curr_row == 1:
            row_spot += 1
            tot_spot += (row-col) * row_spot

            for key in d.keys(): # only key
                if tot_spot >= d[key]:
                    print(0)
                    break
                else:
                    print(tot_spot-d[key])
                    break
        keys = d.keys()
        for key in keys:
            d[key] -= 1
            if d[key] == 0:
                del d[key]

        row += curr_row-1
        col += 1
        row_spot += (curr_row-1)//2
        tot_spot += row_spot * col
    return

prob_f(jockeys)