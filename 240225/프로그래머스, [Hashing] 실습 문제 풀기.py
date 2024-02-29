from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    # 신고자가 신고한 사람을 적을 딕셔너리와(value값 set)
    # 신고당한 사람이 몇번 신고당했는지 계산할 딕셔너리(value값 int)
    reporter, check = defaultdict(set), defaultdict(int)
    for user in report:
        # a가 b를 신고하면
        a, b = user.split()
        # a의 set에 신고한 명단 b를 추가하고
        reporter[a].add(b)
        # b의 신고 받은 횟수를 1 증가한다
        check[b] += 1
    for id in id_list:
        ck = 0
        # id가 신고한 사람들 중에
        for now in reporter[id]:
            # 신고 받은 횟수가 k 이상인 사람이 있다면
            if check[now] >= k:
                # 결과 메일을 받은 횟수 1 증가한다
                ck += 1
        answer.append(ck)
    return answer

import sys

id = list(sys.stdin.readline().strip().split('", "'))
re = list(sys.stdin.readline().strip().split('","'))
k = int(sys.stdin.readline())
print(solution(id, re, k))