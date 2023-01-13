import sys
N = int(sys.stdin.readline())
pic = [[['']*7 for _ in range(5)] for _ in range(N)]
for i in range(N):
    for j in range(5):
        pic[i][j] = list(sys.stdin.readline().rstrip())
cnt = 36
for i in range(N):
    for j in range(i+1, N):
        now = 0
        for x in range(5):
            for y in range(7):
                if pic[i][x][y] != pic[j][x][y]:
                    now += 1
        if cnt > now:
            cnt = now
            start, end = i+1, j+1
print(start, end)