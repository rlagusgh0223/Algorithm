import sys
N, M = map(int, sys.stdin.readline().split())
game = [int(sys.stdin.readline()) for _ in range(N)]
referee = [int(sys.stdin.readline()) for _ in range(M)]
ans = [0] * N
for i in range(M):
    for j in range(N):
        if referee[i] >= game[j]:
            ans[j] += 1
            break
print(ans.index(max(ans))+1)