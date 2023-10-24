# 플로이드-워셜로 작성한 코드
# 데이크스트라에 비해서 이게 더 느리다
import sys
n, m, r = map(int, sys.stdin.readline().split())
items = [0] + list(map(int, sys.stdin.readline().split()))
distance = [[int(1e9)]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    distance[i][i] = 0

for i in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    distance[a][b] = min(distance[a][b], l)
    distance[b][a] = min(distance[b][a], l)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

ans = 0
for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        if distance[i][j] <= m:
            temp += items[j]
    ans = max(ans, temp)

print(ans)