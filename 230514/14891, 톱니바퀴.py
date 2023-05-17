def DFS(index, dir, rot, move):
    if index<3 and dir=='R':
        if gears[index][2] != gears[index+1][6]:
            DFS(index+1, dir, rot*-1, True)
    elif index>0 and dir=='L':
        if gears[index-1][2] != gears[index][6]:
            DFS(index-1, dir, rot*-1, True)
    if move:
        rotate(index, rot)

def rotate(index, rot):
    result = [0] * 8
    if rot == 1:
        for i in range(8):
            result[(i+1)%8] = gears[index][i]
    else:
        for i in range(8):
            result[(i-1)%8] = gears[index][i]
    gears[index] = result

import sys
gears = [[] for _ in range(4)]
for i in range(4):
    gear = list(sys.stdin.readline().rstrip())
    for g in gear:
        gears[i].append(int(g))
K = int(sys.stdin.readline())
for _ in range(K):
    index, rot = map(int, sys.stdin.readline().split())
    index -= 1
    DFS(index, "R", rot, False)
    DFS(index, "L", rot, True)
ans = 0
for i in range(4):
    if gears[i][0] == 1:
        ans += 2**i
print(ans)