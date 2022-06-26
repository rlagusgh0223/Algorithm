from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
man = deque(list(int(i)+1 for i in range(N)))
lst = []
cnt = 0

while man:
  now = man.popleft()
  cnt += 1
  if cnt == K:
    cnt = 0
    lst.append(now)
  else:
    man.append(now)

print("<", end='')
for i in range(len(lst)-1):
  print(lst[i], end='')
  print(", ", end='')
print(lst[len(lst)-1], end='')
print(">")