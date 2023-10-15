from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
wheel = deque(['?']*N)
for _ in range(K):
    S, word = sys.stdin.readline().split()
    for _ in range(int(S)):
        # HONITAVR 을 시계방향으로 한 칸 움직이면
        # RHONITAV 가 된다
        wheel.appendleft(wheel.pop())
    if wheel[0]=='?' and word not in wheel:
        wheel[0] = word
    elif wheel[0] == word:
        continue
    else:
        wheel[0] = '!'
if '!' in wheel:
    print('!')
else:
    print(*wheel, sep='')