import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
lst = deque([int(x) for x in range(1, N+1)])
answer = []
cnt = 0
while lst:
    cnt += 1
    now = lst.popleft()
    if cnt == K:
        cnt = 0
        answer.append(str(now))
    else:
        lst.append(now)
print("<", end='')
print(', '.join(answer), end='')
print('>')