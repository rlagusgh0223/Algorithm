# 집합 문제라서 집합으로 풀긴 했는데 이게 시간이 좀 더 걸린다...
import sys
M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    check = sys.stdin.readline().split()
    if len(check)==2:
        ck, x = check[0], int(check[1])
        if ck == 'add':
            S.add(x)
        elif ck == 'remove':
            if x in S:
                S.discard(x)
        elif ck == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif ck == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
    else:
        if check[0] == 'all':
            S = set(list(range(1, 21)))
        else:
            S = set()