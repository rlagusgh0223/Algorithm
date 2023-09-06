def check(lst, mid):
    # 시작/끝 부분과 각 가로등 사이의 거리를 가로등이 다 밝히지 못하는 거리면 0리턴
    # m은 모든 구간의 거리 이상이어야 한다
    if lst[1] - lst[0] > mid:
        return 0
    if lst[-1] - lst[-2] > mid:
        return 0
    for i in range(1, len(lst) - 2):
        if (lst[i+1] - lst[i]) / 2 > mid:
            return 0
    return 1

import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
lst = [0] + list(map(int, sys.stdin.readline().split())) + [N]
ans = 0
start, end = 0, N
while start <= end:
    mid = (start + end) // 2
    if check(lst, mid):
        end = mid - 1
        ans = mid
    else:
        start = mid + 1
print(ans)