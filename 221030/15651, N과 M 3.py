def go(index, n, m):
    if index == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N+1):
        answer[index] = i
        go(index+1, N, M)

import sys
N, M = map(int, sys.stdin.readline().split())
answer = [0] * M
go(0, N, M)