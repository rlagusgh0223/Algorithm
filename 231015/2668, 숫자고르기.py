def DFS(first, second, num):
    first.add(num)
    second.add(lst[num])
    if lst[num] in first:
        if first == second:
            ans.update(first)  # set에서의 update는 여러개의 값을 추가할때 사용한다
            return True
        return False
    DFS(first, second, lst[num])

import sys
N = int(sys.stdin.readline())
lst = [0] * (N+1)
for i in range(1, N+1):
    lst[i] = int(sys.stdin.readline())
ans = set()
for i in range(1, N+1):
    if i not in ans:
        DFS(set(), set(), i)
print(len(ans))
print(*sorted(list(ans)), sep='\n')