from collections import deque
N, K = map(int, input().split())
man = deque([int(i) for i in range(1, N+1)])
answer = []
cnt = 0

while man:
  cnt += 1
  now = man.popleft()
  if cnt == K:
    answer.append(str(now))
    cnt = 0
  else:
    man.append(now)

print("<", end='')
print(", ".join(answer), end='')
print(">")