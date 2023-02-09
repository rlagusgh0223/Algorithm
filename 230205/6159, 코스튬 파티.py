# pypy3로 해야 시간초과 안 걸린다
import sys
N, S = map(int, sys.stdin.readline().split())
lst = [0] * N
cnt = 0
for i in range(N):
    lst[i] = int(sys.stdin.readline())
lst.sort()
for i in range(N-1):
    if lst[i] >= S//2:
        break
    for j in range(i+1, N):
        if lst[i]+lst[j] <= S:
            cnt += 1
        else:
            break
print(cnt)