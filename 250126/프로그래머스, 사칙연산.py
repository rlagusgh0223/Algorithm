def solution(arr):
    arr = list((''.join(arr)).split("-"))
    a1 = sum(map(int, arr[0].split("+")))
    maxarr = minarr = 0
    for a in arr[:0:-1]:
        x = list(map(int, a.split("+")))
        minx = -sum(x)
        maxx = -x[0] + sum(x[1:])
        # 누적된 최솟값은 현재최솟값+누적최솟값 또는 현재최솟값-누적최댓값 중에서 구하고
        # 누적된 최댓값은 현재최댓값+누적최댓값 또는 현재최솟값-누적최솟값으로 계산한다
        # 변수에 있는 값이 음수일 경우도 있으므로 --해서 +가 되거나 +-로 -가 되는 경우도 있기 때문이다
        minarr, maxarr = min(minx+minarr, minx-maxarr), max(maxx+maxarr, minx-minarr)
    return a1 + maxarr

import sys

print(solution(list(sys.stdin.readline().strip().split('", "'))))
