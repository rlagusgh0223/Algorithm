from collections import deque
import sys

N = int(sys.stdin.readline())
card = deque([int(n) for n in range(1, N+1)])

while len(card)>1:
    card.popleft()
    card.append(card.popleft())

print(card[0])