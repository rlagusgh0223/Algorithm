from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
lst = deque([int(i)+1 for i in range(N)])
man = []
cnt = 0
while lst:
  cnt += 1
  now = lst.popleft()
  if cnt == K:
    man.append(str(now))
    cnt = 0
  else:
    lst.append(now)

print("<", end='')
print(", ".join(man), end='')
print(">")