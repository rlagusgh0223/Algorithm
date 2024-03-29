import sys

def DFS(idx, sum):
    global answer
    if idx == N:
        return
    sum += arr[idx]
    if sum == S:
        answer += 1
    DFS(idx+1, sum-arr[idx])
    DFS(idx+1, sum)

N, S = map(int, sys.stdin.readline().split())
arr = [int(x) for x in sys.stdin.readline().split()]
answer = 0
DFS(0, 0)
print(answer)