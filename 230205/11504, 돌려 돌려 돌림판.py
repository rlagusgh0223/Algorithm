import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    X = input().split()
    Y = input().split()
    lst = list(input().split()) * 2
    cnt = 0
    x = int(''.join(X))
    y = int(''.join(Y))
    for i in range(N):
        Z = ''
        for j in range(M):
            Z += lst[i+j]
        if x <= int(''.join(Z)) <= y:
            cnt += 1
    print(cnt)