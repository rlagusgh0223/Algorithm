from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
visit = [0] * (n+1)
visit[start] = 1

q = deque()
q.append(start)
while q:
    x = q.popleft()
    for y in arr[x]:
        if visit[y] == 0:
            visit[y] = visit[x]+1
            q.append(y)

print(visit[end]-1 if visit[end]!=0 else -1)


# 답은 잘 나오는데 틀렸다고 한다
# 9
# 7 6
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 3 5
# 5 6
# from collections import deque
# def bfs():
#     q = deque()
#     q.append((start, 1))  # 현재 사람, 촌수
#     while q:
#         x, cnt = q.popleft()
#         if family[x][end] == 1:
#             for now in family:
#                 print(now)
#             return cnt
#         for i in range(1, 10):
#             if family[x][i] == 1:
#                 q.append((i, cnt+1))
#                 family[x][i] = cnt+1
#     return -1

# import sys
# input = sys.stdin.readline
# n = int(input())
# start, end = map(int, input().split())  # 촌수 계산
# m = int(input())
# family = [[0]*(n+1) for _ in range(n+1)]
# for i in range(m):
#     x, y = map(int, input().split())
#     family[x][y] = family[y][x] = 1
# print(bfs())