import sys
N = int(sys.stdin.readline())
for i in range(1, N):
    n = 1 + i + i*i
    if n == N:
        print(i)           
        exit()