def DFS(idx, sum):
    global answer
    if idx == N:
        return int(idx)
    sum += arr[idx]
    if S == sum:
        answer += 1
    DFS(idx+1, sum-arr[idx])
    DFS(idx+1, sum)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
DFS(0, 0)
print(answer)