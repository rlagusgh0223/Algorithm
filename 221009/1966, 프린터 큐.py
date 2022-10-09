import sys
T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    index = [int(x) for x in range(N)]
    cnt = 0
    while lst:
        if lst[0] == max(lst):
            lst.pop(0)
            now = index.pop(0)
            cnt += 1
            if now == M:
                print(cnt)
        else:
            lst.append(lst.pop(0))
            index.append(index.pop(0))