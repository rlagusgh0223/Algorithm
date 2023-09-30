import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
check = [0] * (n+1)
ans = 0
lst = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)
for now in lst[1]:
    check[now] = 1
    for nxt in lst[now]:
        if check[nxt] == 0:
            check[nxt] = 1
check[1] = 0
print(sum(check))



# BFS로 만들수는 있는데 어차피 한번만 더 들어가는데(친구의 친구) 뭐하러 BFS를 하나 싶다
# def BFS(now):
#     q = deque()
#     for n in lst[now]:
#         q.append(n)
#         check[n] = 1
#     while q:
#         x = q.popleft()
#         for n in lst[x]:
#             if check[n] == 0:
#                 check[n] = check[x] + 1
#                 q.append(n)

# from collections import deque
# import sys
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# check = [0] * (n+1)
# lst = [[] for _ in range(n+1)]
# ans = 0
# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     lst[a].append(b)
#     lst[b].append(a)
# BFS(1)
# for i in range(2, n+1):
#     if 1 <= check[i] <= 2:  # 본인의 친구(1)거나, 친구의 친구(2)
#         ans += 1
# print(ans)