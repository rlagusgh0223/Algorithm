import sys
N, K = map(int, sys.stdin.readline().split())
lst = [0, 1] + list(range(2, N+1))
for i in range(2, N+1):
    j = 1
    while i*j <= N:
        if lst[i*j] != 0:
            lst[i*j] = 0
            K -= 1
            if K == 0:
                print(i*j)
                exit()
        j += 1