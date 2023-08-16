import sys, copy
from collections import deque
input = sys.stdin.readline

# 양분 그래프 n x n, m 나무개수, k년이 지난 후
n, m, k = map(int, input().split())

# 나중에 겨울에 양분 추가해줄 그래프 = plus_soil
plus_soil = []
for _ in range(n):
    plus_soil.append(list(map(int, input().split())))

# 나무 양분 그래프
origin_soil = [[5] * n for _ in range(n)]

# 살아있는 나무 그래프
live = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    live[x - 1][y - 1].append(z)

for _ in range(k):
    # 봄 + 여름
    for i in range(n):
        for j in range(n):
            if live[i][j]:
                # 봄에 나이가 어린 나무 부터 양분을 먹게 하기 위한 정렬
                live[i][j].sort()
                # 살아있는 나무들 리스트를 알아야 가을에 번식을 할 수 있다
                tmp_live_tree = []
                death = 0
                for age in live[i][j]:
                    if age <= origin_soil[i][j]:
                        origin_soil[i][j] -= age
                        age += 1
                        tmp_live_tree.append(age)
                    else:
                        death += age // 2
                origin_soil[i][j] += death
                # 죽은건 죽은대로, 산건 산거대로 옮긴다
                live[i][j].clear()
                live[i][j].extend(tmp_live_tree)

    # 가을
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    for i in range(n):
        for j in range(n):
            if live[i][j]:
                for age in live[i][j]:
                    if age % 5 == 0:
                        for dir in range(8):
                            nx, ny = i+dx[dir], j+dy[dir]
                            if 0 <= nx < n and 0 <= ny < n:
                                live[nx][ny].append(1)

    # 겨울
    for i in range(n):
        for j in range(n):
            origin_soil[i][j] += plus_soil[i][j]

result = 0
for i in range(n):
    for j in range(n):
        result += len(live[i][j])
print(result)


# 아래 코드가 시간도 많이 걸리고 메모리도 많이 차지하지만 더 보기 쉬워보여서 참고용으로 남긴다
# from collections import deque

# n, m, k = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# graph = [[5] * n for _ in range(n)]
# trees = [[deque() for _ in range(n)] for _ in range(n)]
# dead_trees = [[list() for _ in range(n)] for _ in range(n)]
# for _ in range(m):
#     x, y, z = map(int, input().split())
#     trees[x - 1][y - 1].append(z)

# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]

# def spring_summer():
#     for i in range(n):
#         for j in range(n):
#             len_ = len(trees[i][j])
#             for k in range(len_):
#                 if graph[i][j] < trees[i][j][k]:
#                     for _ in range(k, len_):
#                         dead_trees[i][j].append(trees[i][j].pop())
#                     break
#                 else:
#                     graph[i][j] -= trees[i][j][k]
#                     trees[i][j][k] += 1
#     for i in range(n):
#         for j in range(n):
#             while dead_trees[i][j]:
#                 graph[i][j] += dead_trees[i][j].pop() // 2

# def fall_winter():
#     for i in range(n):
#         for j in range(n):
#             for k in range(len(trees[i][j])):
#                 if trees[i][j][k] % 5 == 0:
#                     for l in range(8):
#                         nx, ny = i + dx[l], j + dy[l]
#                         if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                             continue
#                         trees[nx][ny].appendleft(1)
#             graph[i][j] += a[i][j]

# for i in range(k):
#     spring_summer()
#     fall_winter()

# answer = 0
# for i in range(n):
#     for j in range(n):
#         answer += len(trees[i][j])

# print(answer)