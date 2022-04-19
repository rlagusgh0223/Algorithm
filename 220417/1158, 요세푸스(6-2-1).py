# LinkedList 예제이지만 코딩테스트에서는 잘 나오지 않는 주제이니 개념만 정리하자
from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
q = deque()
lst = []
for i in range(1, N+1):
    q.append(i)

while q:
    for i in range(K):
        if i == K-1:
            x = q.popleft()
            lst.append(x)
        else:
            x = q.popleft()
            q.append(x)

print('<', end='')
for i in range(len(lst)):
    if i == len(lst)-1:
        print(lst[i], end='')
    else:
        print(lst[i], end=', ')
print('>')