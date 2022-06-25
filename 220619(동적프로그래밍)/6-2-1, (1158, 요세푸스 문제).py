from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
lst = deque([int(i) for i in range(1, N+1)])
answer = []

cnt = 0
while lst:
  now = lst.popleft()
  cnt += 1
  if cnt == K:
    answer.append(str(now))    # join은 문자열만 되지, int형으로 하면 에러 난다
    cnt = 0
  else:
    lst.append(now)

print("<", end='')    # ,로 구분하면 한 칸 떨어져서 출력된다
print(", ".join(answer), end='')
print(">")