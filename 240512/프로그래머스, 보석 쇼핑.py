# 프로그래밍 강의 Tow pointers 볼 것
from collections import defaultdict


def solution(gems):
    l = 0
    length = 100001
    check = defaultdict(int)    
    size = len(set(gems))
    for r in range(len(gems)):
        check[gems[r]] += 1
        while len(check) == size:
            if r-l+1 < length:
                answer = [l+1, r+1]
                length = r-l+1
            check[gems[l]] -= 1
            if check[gems[l]] == 0:
                del check[gems[l]]
            l += 1
    return answer

import sys

gems = list(sys.stdin.readline().strip().split('", "'))
print(solution(gems))