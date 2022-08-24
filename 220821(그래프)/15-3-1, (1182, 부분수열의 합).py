from collections import deque
import sys

def DFS(idx, sum):
    global answer
    if idx==N:
        return
    sum += arr[idx]
    if S == sum:
        answer += 1
    DFS(idx+1, sum-arr[idx])
    DFS(idx+1, sum)

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
temp = [[0 for _ in range(N+1)] for _ in range(N+1)]
answer = 0
visit = [0]*(N+1)
DFS(0, 0)
print(answer)