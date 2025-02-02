from collections import defaultdict


def solution(genres, plays):
    answer = []
    d1, d2 = defaultdict(list), defaultdict(int)
    for i, (g, p) in enumerate(zip(genres, plays)):
        d1[g].append((i, p))
        d2[g] += p
    for g, p in sorted(d2.items(), key=lambda x:x[1], reverse=True):
        # 한 장르당 최대 두 개까지 베스트 앨범을 구하는 것이므로 [:2]를 쓴다
        for i, p in sorted(d1[g], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    return answer


import sys

g = list(sys.stdin.readline().strip().split('", "'))
p = list(map(int, sys.stdin.readline().split(", ")))
print(solution(g, p))