vents = open("input.txt", "r")
vents = [i for i in vents]

map = [[0 for i in range(1000)] for j in range(999)]


def order_values(i, j):
    if i > j:
        return (j, i)
    else:
        return (i, j)


for vent in vents:
    startX, startY, endX, endY = [int(x) for x in vent.replace(" -> ", ",").split(",")]
    startX, endX = order_values(startX, endX)
    startY, endY = order_values(startY, endY)
    if startX == endX:
        for y in range(startY, endY+1):
            map[startX][y] += 1
    elif startY == endY:
        for x in range(startX, endX+1):
            map[x][startY] += 1
    else:
        for n, x in enumerate(range(startX, endX+1)):
            y = startY + n
            map[x][y] += 1

count = 0
for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j] > 1:
            count += 1

print(count)
