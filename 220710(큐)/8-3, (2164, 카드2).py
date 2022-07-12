from collections import deque
import sys

N = int(sys.stdin.readline())
card = deque(list(int(now) for now in range(N, 0, -1)))

while len(card) != 1:
    card.pop()
    card.appendleft(card.pop())

print(card[0])