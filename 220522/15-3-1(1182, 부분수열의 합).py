# 한번 더
import sys
N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
score = 0

def DFS(now, sum):
    global score
    if now == N:
        return
    sum += lst[now]
    if sum == S:
        score += 1
    DFS(now+1, sum-lst[now])
    DFS(now+1, sum)

DFS(0, 0)
print(score)