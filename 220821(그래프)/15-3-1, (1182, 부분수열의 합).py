def DFS(idx, sum):
    global cnt
    if idx==N:
        return
    sum += arr[idx]
    if S == sum:
        cnt += 1
    DFS(idx+1, sum-arr[idx])
    DFS(idx+1, sum)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
DFS(0, 0)
print(cnt)