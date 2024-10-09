from itertools import combinations


def solution(relation):
    answer = []
    n = len(relation[0])
    for i in range(1, n+1):
        for comb in combinations(range(n), i):
            # 유일성 확인
            unique = set(tuple(r[c] for c in comb)for r in relation)
            if len(unique) == len(relation):
                # 최소성 확인
                # issubset : a가 comb의 부분집합인지 확인
                if not any(set(a).issubset(set(comb)) for a in answer):
                    answer.append(comb)
    return len(answer)

import sys

relation = list(sys.stdin.readline().strip().split('"],["'))
relation = [list(r.split('","')) for r in relation]
print(solution(relation))