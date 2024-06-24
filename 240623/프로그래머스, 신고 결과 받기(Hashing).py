from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    # 한 사람이 동일한 사람에게 신고한 경우를 없애기 위해 set()으로 중복 제거
    report = list(set(report))
    # 각 사람별 신고한 사람, 신고받은 횟수를 저장할 딕셔너리
    # defaultdict을 이용하면 초기값이 세팅되서 만들어진다
    check, num = defaultdict(list), defaultdict(int)
    for r in report:
        x, y = r.split()
        check[x].append(y)
        num[y] += 1
    for id in id_list:
        mail = 0
        # 이 사람(id)이 신고한 사람(check[id]) 중 k번 이상 신고당한 사람이 있다면
        # 메일 받는 횟수 1 증가
        for c in check[id]:
            if num[c] >= k:
                mail += 1
        answer.append(mail)
    return answer

import sys

id_list = list(sys.stdin.readline().strip().split('", "'))
report = list(sys.stdin.readline().strip().split('", "'))
k = int(sys.stdin.readline())
print(solution(id_list, report, k))