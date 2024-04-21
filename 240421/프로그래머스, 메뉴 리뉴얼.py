# Counter : 리스트에 원소가 몇 번 나왔는지 세 줌
from collections import Counter
# combinations : 순서를 고려하지 않고 중복없이 뽑는다
from itertools import combinations


def solution(orders, course):
    answer = []
    # course 배열의 수 만큼 글자들의 조합이 있는지 확인
    for c in course:
        check = []
        # 각각의 문자열들을 course 배열의 현재 값 만큼 조합하여 check에 입력
        for order in orders:
            # 현재 order에서 c만큼의 숫자로 가능한 모든 배열 생성
            for menu in combinations(order, c):
                res = ''.join(sorted(menu))
                check.append(res)
        # 후보 메뉴 조합들의 빈도를 카운트 하고 많은 순으로 정렬
        result = Counter(check).most_common()
        # 가장 많이 나온 조합을 선택
        # 2번 이상 나오고 그 빈도가 가장 큰 메뉴 조합과 동일한 빈도를 가진 경우 answer에 추가
        answer += [r for r, cnt in result if cnt>1 and cnt==result[0][1]]
    return sorted(answer)


import sys

orders = list(sys.stdin.readline().strip().split('", "'))
course = list(map(int, sys.stdin.readline().split(",")))
print(solution(orders, course))