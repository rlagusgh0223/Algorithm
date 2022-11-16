from collections import deque
import sys
N = int(sys.stdin.readline())
router = deque()
while True:
    packet = int(sys.stdin.readline())
    if packet == 0:
        if not router:
            continue
        router.popleft()
    elif packet == -1:
        break
    elif len(router) >= N:
        continue
    else:
        router.append(packet)
if not router:
    print("empty")
else:
    print(' '.join(map(str, router)))