from collections import deque
n = int(input())
a = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)
order = [int(x)-1 for x in input().split()]
check = [False] * n
parent = [-1] * n
q = deque()
q.append(0)
check[0] = True
m = 1
for i in range(n):
    if not q:
        print(0)
        exit()
    x = q.popleft()
    if x != order[i]:
        print(0)
        exit()
    cnt = 0
    for y in a[x]:
        if check[y] == False:
            parent[y] = x
            cnt += 1
    for j in range(cnt):
        if m+j>=n or parent[order[m+j]]!=x:
            print(0)
            exit()
        q.append(order[m+j])
        check[order[m+j]] = True
    m += cnt
print(1)