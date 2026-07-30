x, t, vh, vg = map(int, input().split())

shot_han = -1000 / vh
shot_greedo = t - (x ** 2 + 1000 ** 2) ** 0.5 / vg

print("HAN" if shot_han < shot_greedo else "GREEDO")