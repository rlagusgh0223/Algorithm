def solution(arr):
    # 2**0 == 1
    # arr의 길이도 1부터라고 했으므로 맨 처음값을 1로 시작한다
    check = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    if len(arr) in check:
        return arr
    for i in range(len(check)):
        if len(arr) < check[i]:
            arr += [0] * (check[i] - len(arr))
            return arr

import sys

arr = list(map(int, sys.stdin.readline().split(", ")))
print(solution(arr))