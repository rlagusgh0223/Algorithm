def solution(genres, plays):
    answer = []
    dic1, dic2 = {}, {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        # 장르별로 노래를 나눌 dic
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))
        # 장르별 play 총합을 넣을 dic
        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    # 장르별로 노래 총합(x[1])이 많은것부터 출력한다
    # genre는 장르, play는 총 플레이 수
    # items() : {key:value} 형태를 {(key, value)} 형태로 만들어 준다
    # key=lambda x:x[1] : value값으로 정렬해준다
    for genre, play in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        # 해당장르 중 플레이가 많은것(x[1])부터 2번째까지만 출력한다
        # index는 해당 노래의 번호, p는 플레이 수
        for index, p in sorted(dic1[genre], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(index)
    return answer

import sys
genres = list(sys.stdin.readline().strip().split('", "'))
plays = list(map(int, sys.stdin.readline().strip().split(", ")))
print(solution(genres, plays))