# data.index(num) <= len(data)//2를 만족하면 왼쪽으로 이동시키고
# 반대의 경우 오른쪽으로 이동시켜야 이동횟수를 최소화 시킬 수 있다

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
index = deque([int(x) for x in range(1, N+1)])
cnt = 0
for now in lst:
    while True:
        if index[0] == now:
            index.popleft()
            break
        else:
            # .index : 리스트의 몇번째에 특정한 원소가 처음 등장했는지 알려줌
            if index.index(now) <= len(index)//2:  
                index.append(index.popleft())
                cnt += 1
            else:
                index.appendleft(index.pop())
                cnt += 1
print(cnt)