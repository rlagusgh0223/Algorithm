from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
queue = deque()
lst = deque([int(card) for card in range(N, 0, -1)])

while len(lst)>1:
    lst.pop()
    lst.appendleft(lst.pop())

print(lst[0])