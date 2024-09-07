from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    check, num = defaultdict(list), defaultdict(int)

    for r in report:
        x, y = r.split()
        check[x].append(y)
        num[y] += 1
    
    for id in id_list:
        mail = 0
        for ck in check[id]:
            if num[ck] >= k:
                mail += 1
        answer.append(mail)
        
    return answer

import sys

id_list = list(sys.stdin.readline().strip().split('", "'))
report = list(sys.stdin.readline().strip().split('", "'))
k = int(sys.stdin.readline())
print(solution(id_list, report, k))