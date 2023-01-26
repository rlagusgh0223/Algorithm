import sys
N, M = map(int, sys.stdin.readline().split())
lst = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
cnt = 0
ans = []
for j in range(M):
    ck = [0, 0, 0, 0]
    for i in range(N):
        if lst[i][j] == 'A':
            ck[0] += 1
        elif lst[i][j] == 'C':
            ck[1] += 1
        elif lst[i][j] == 'G':
            ck[2] += 1
        elif lst[i][j] == 'T':
            ck[3] += 1
    if max(ck) == ck[0]:
        ans.append('A')
    elif max(ck) == ck[1]:
        ans.append('C')
    elif max(ck) == ck[2]:
        ans.append('G')
    else:
        ans.append('T')
    cnt += sum(ck) - max(ck)
print(*ans, sep='')
print(cnt)


# from collections import Counter
# import sys
# N, M = map(int, sys.stdin.readline().split())
# lst1 = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# lst2 = [['']*N for _ in range(M)]
# ans = []
# cnt = 0
# for i in range(M):
#     for j in range(N):
#         lst2[i][j] = lst1[j][i]
#     lst2[i].sort()
# for i in range(M):
#     nmax = Counter(lst2[i]).most_common(1)
#     ck = nmax[0][0]
#     ans.append(ck)
#     for j in range(N):
#         if lst2[i][j] != ck:
#             cnt += 1
# print(*ans, sep='')
# print(cnt)