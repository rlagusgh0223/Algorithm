from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())

human = deque([int(i)+1 for i in range(N)])
cnt = 0
answer = []

while human:
  cnt += 1
  now = human.popleft()
  if cnt == K:
    answer.append(str(now))
    cnt = 0
  else:
    human.append(now)

print("<", end='')
print(", ".join(answer), end='')
print(">")