import sys
N = int(sys.stdin.readline())
mirror = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
K = int(sys.stdin.readline())
for i in range(N):
    if K == 1:
        print(*mirror[i], sep='')
    elif K == 2:
        print(*mirror[i][::-1], sep='')
    elif K == 3:
        print(*mirror[N-1-i], sep='')