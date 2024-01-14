def solution(lottos, win_nums):
    answer = [0]*2
    check = 0
    for lotto in lottos:
        if lotto in win_nums:
            check += 1
    answer[0], answer[1] = min(6, 7-(lottos.count(0)+check)), min(6, 7-check)
    return answer

import sys
lotto = list(map(int, sys.stdin.readline().split(", ")))
win = list(map(int, sys.stdin.readline().split(", ")))
print(solution(lotto, win))