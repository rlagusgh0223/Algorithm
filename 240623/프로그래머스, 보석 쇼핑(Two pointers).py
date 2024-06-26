from collections import defaultdict


def solution(gems):
    l = 0  # 점검 시작 위치
    jewelry = len(set(gems))  # 보석 종류
    length = 100000  # 보석 구간 길이, len(gems)로 하면 에러 난다
    check = defaultdict(int)  # 구간 내의 보석 종류 및 보석 수를 기록할 딕셔너리
    for r in range(len(gems)):
        check[gems[r]] += 1  # 이번 순서의 보석 구간 내에 추가
        # 지금 보석 구간 내에 모든 보석의 종류가 들어있다면
        while len(check) == jewelry:
            # 현재 구간의 길이가 기존 구간의 길이보다 짧을 경우
            # 새로 입력한다
            if r-l+1 < length:
                answer = [l+1, r+1]
                length = r-l+1
            # 종료지점이 동일한 가운데
            # 시작지점을 한 칸 우로 이동해서
            # 구간 길이를 줄이고 검사해본다
            check[gems[l]] -= 1
            if check[gems[l]] == 0:
                del check[gems[l]]
            l += 1
    return answer

import sys

print(solution(list(sys.stdin.readline().strip().split('", "'))))
