# 기존의 방식보다 이게 좀 더 시간이 빠르다
def go(index, n, m):
    if index == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N+1):
        if c[i]:
            continue
        c[i] = True
        answer[index] = i
        go(index+1, n, m)
        c[i] = False

import sys
N, M = map(int, sys.stdin.readline().split())
c = [False] * (N+1)
answer = [0] * M
go(0, N, M)