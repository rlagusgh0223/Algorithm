graph = [[int(now) for now in input().split()] for _ in range(9)]
cnt = -1
for i in range(9):
    for j in range(9):
        if cnt < graph[i][j]:
            cnt = graph[i][j]
            x, y = i+1, j+1
print(cnt)
print(x, y)