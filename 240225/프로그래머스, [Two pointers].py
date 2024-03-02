from collections import defaultdict


def solution(gems):
    l = 0
    length = 10000000
    check = defaultdict(int)
    # while문에서 체크할때마다 gems의 길이를 계산하면 시간초과 나온다
    end = len(set(gems))
    for r in range(len(gems)):
        # dict()은 존재하지 않는 키에 접근하려고 하면 에러가 나지만
        # (초기값을 같이 입력한 경우 제외)
        # defaultdict()은 존재하지 않는 키의 경우
        # ()안의 값에 맞춰 초기값을 사용하여 키를 생성한다
        check[gems[r]] += 1
        while len(check) == end:
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