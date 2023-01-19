import sys
N = int(sys.stdin.readline())
lst = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        if lst[i] == lst[j][::-1]:
            now = len(lst[i])
            print(now)
            print(lst[i][now//2])
            break