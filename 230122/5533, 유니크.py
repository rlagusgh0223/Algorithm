import sys
N = int(sys.stdin.readline())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = [0]*N
for i in range(3):
    for j in range(N):
        ck = True
        for k in range(N):
            if j == k:
                continue
            if s[j][i] == s[k][i]:
                ck = False
                break
        if ck:
            ans[j] += s[j][i]
print(*ans, sep='\n')

# 시간은 이게 더 걸리고 메모리는 동일하다
# import sys
# N = int(sys.stdin.readline())
# s = [[0]*N for _ in range(3)]
# for i in range(N):
#     a, b, c = map(int, sys.stdin.readline().split())
#     s[0][i] = a
#     s[1][i] = b
#     s[2][i] = c
# ans = [0]*N
# for i in range(3):
#     for j in range(N):
#         if s[i].count(s[i][j])==1:
#             ans[j] += s[i][j]
# print(*ans, sep='\n')