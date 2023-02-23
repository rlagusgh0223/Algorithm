import sys
x, y = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
ans = []
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        for k in range(3):
            if i==k or j==k:
                continue
            cnt = ((lst[i][0]-x)**2+(lst[i][1]-y)**2)**0.5 + ((lst[j][0]-lst[i][0])**2+(lst[j][1]-lst[i][1])**2)**0.5 + ((lst[k][0]-lst[j][0])**2+(lst[k][1]-lst[j][1])**2)**0.5
            ans.append(int(cnt))
print(min(ans))