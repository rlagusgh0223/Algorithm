from collections import defaultdict


def solution(gems):
    l = 0
    kind = len(set(gems))
    length = len(gems)+1
    check = defaultdict(int)
    for r in range(len(gems)):
        check[gems[r]] += 1
        while len(check) == kind:
            if r-l+1 < length:
                length = r-l+1
                answer = [l+1, r+1]
            
            check[gems[l]] -= 1
            if check[gems[l]] == 0:
                del check[gems[l]]
            l += 1
    return answer

import sys

gems = list(sys.stdin.readline().strip().split('", "'))
print(solution(gems))