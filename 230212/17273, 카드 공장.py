# 시간은 조금 더 걸리지만 더 직관적인 코드라 가져왔다
import sys
N, M = map(int, sys.stdin.readline().split())
f = [0] * N
b = [0] * N
now = [0] * N
for i in range(N):
    f[i], b[i] = map(int, sys.stdin.readline().split())
    now[i] = f[i]
for _ in range(M):
    K = int(sys.stdin.readline())
    for i in range(N):
        if now[i] <= K:
            if now[i] == f[i]:
                now[i] = b[i]
            else:
                now[i] = f[i]
print(sum(now))


# import sys
# N, M = map(int, sys.stdin.readline().split())
# ck = [0] * N
# now = [0] * N
# card = [[0, 0] for _ in range(N)]
# for i in range(N):
#     card[i][0], card[i][1] = map(int, sys.stdin.readline().split())
#     now[i] = card[i][0]
# for _ in range(M):
#     K = int(sys.stdin.readline())
#     for i in range(N):
#         if now[i] <= K:
#             now[i] = card[i][(ck[i]+1)%2]
#             ck[i] = (ck[i]+1)%2
# print(sum(now))

# 예제
# 5 3
# 4 6
# 9 1
# 8 8
# 4 2
# 3 7
# 8
# 2
# 9