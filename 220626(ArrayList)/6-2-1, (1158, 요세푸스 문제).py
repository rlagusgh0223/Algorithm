from collections import deque
N, K = map(int, input().split())
human = deque([int(x) for x in range(1, N+1)])
lst = []
cnt = 0

while human:
  cnt += 1
  now = human.popleft()
  if cnt == K:
    cnt = 0
    lst.append(str(now))
  else:
    human.append(now)

print("<", end='')
print(", ".join(lst), end='')
print(">")