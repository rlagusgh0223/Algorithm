def DFS(chk, hop):
    global answer
    if chk == N:
        return
    hop += arr[chk]
    if S == hop:
        answer += 1
    DFS(chk+1, hop-arr[chk])
    DFS(chk+1, hop)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
DFS(0, 0)
print(answer)