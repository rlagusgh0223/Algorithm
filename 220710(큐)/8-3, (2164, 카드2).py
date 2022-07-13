from collections import deque
import sys
N = int(sys.stdin.readline())
queue = deque([int(card) for card in range(1, N+1)])

while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])