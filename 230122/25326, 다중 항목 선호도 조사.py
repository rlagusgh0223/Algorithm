import sys
n, m = map(int, sys.stdin.readline().split())
sfc = [['' for _ in range(n)] for _ in range(3)]
for i in range(n):
    x, y, z = sys.stdin.readline().split()
    sfc[0][i] = x
    sfc[1][i] = y
    sfc[2][i] = z
for i in range(m):
    cnt = 0
    s, f, c = sys.stdin.readline().split()
    for j in range(n):
        if (s=='-' or s==sfc[0][j]) and (f=='-' or f==sfc[1][j]) and (c=='-' or c==sfc[2][j]):
            cnt += 1
    print(cnt)


# import sys
# n, m = map(int, sys.stdin.readline().split())
# sfc = [list(sys.stdin.readline().split()) for _ in range(n)]
# for i in range(m):
#     s, f, c = sys.stdin.readline().split()
#     ans = 0
#     for j in range(n):
#         if (sfc[j][0]==s or s=='-') and (sfc[j][1]==f or f=='-') and (sfc[j][2]==c or c=='-'):
#             ans += 1
#     print(ans)