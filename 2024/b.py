n = int(input())
grsong = {}
for i in range(n):
    group, song = input().split()
    grsong[group] = int(song)
m = int(input())
for j in range(m):
    grsong[input()] -= 1

nosong = True
for group in grsong.keys():
    if grsong[group] > 0:
        nosong = False
        print(group)
        break
if nosong:
    print("NO KPOP FOR VADER")