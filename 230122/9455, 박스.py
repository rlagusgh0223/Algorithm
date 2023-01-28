import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    grid = [[] for _ in range(n)]
    # 입력받은 배열의 열, 행을 바꾸는 코드
    # 기억해 두자
    for i in range(m):
        lst = list(map(int, input().split()))
        for j in range(n):
            grid[j].append(lst[j])
    cnt = 0
    for i in range(n):
        floor = m-1
        for j in range(m-1, -1, -1):
            if grid[i][j] == 1:
                cnt += floor-j
                floor -= 1
    print(cnt)


# 이 코드가 내 코드지만 시간이 훨씬 많이 걸린다
# import sys
# input = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     m, n = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(m)]
#     cnt = 0
#     for j in range(n):
#         ck = True
#         while ck:
#             ck = False
#             for i in range(m-1, 0, -1):
#                 if grid[i][j]==0 and grid[i-1][j]==1:
#                     grid[i][j], grid[i-1][j] = grid[i-1][j], grid[i][j]
#                     cnt += 1
#                     ck = True
#     print(cnt)