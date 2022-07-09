from collections import deque
import sys
N = int(sys.stdin.readline())
queue = deque([int(now) for now in range(1, N+1)])
num = 0
while True:
    if len(queue) == 1:
        break
    queue.popleft()
    num = queue.popleft()
    queue.append(num)
print(queue[0])