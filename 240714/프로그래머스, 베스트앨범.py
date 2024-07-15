from collections import defaultdict


def solution(genres, plays):
    answer = []
    # dic1 : 장르별 인덱스와 해당 순서시 재생횟수를 저장할 딕셔너리
    # dic2 : 장르별 총 재생횟수를 저장할 딕셔너리
    dic1, dic2 = defaultdict(list), defaultdict(int)
    for i, (g, p) in enumerate(zip(genres, plays)):
        dic1[g].append((i, p))
        dic2[g] += p
    # 장르별 총재생횟수가 많은 순서로 반복
    for g, p in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        # 해당 장르에서 많이 재생된 2개의 인덱스만 입력
        for i, p in sorted(dic1[g], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    return answer

import sys

genres = list(sys.stdin.readline().strip().split('", "'))
plays = list(map(int, sys.stdin.readline().split(", ")))
print(solution(genres, plays))