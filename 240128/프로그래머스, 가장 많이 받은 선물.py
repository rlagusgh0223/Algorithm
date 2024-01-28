def solution(friends, gifts):
    answer = [0] * len(friends)
    result = [[0, 0] for _ in range(len(friends))]
    table = [[0]*len(friends) for _ in range(len(friends))]
    
    # 선물 주는거 기록
    for gift in gifts:
        p, g = gift.split()
        tp, tg = friends.index(p), friends.index(g)
        result[tp][0] += 1
        result[tg][1] += 1
        table[tp][tg] += 1
    
    # 선물 지수 계산
    for i in range(len(friends)):
        result[i] = result[i][0] - result[i][1]

    # 선물 더 많이 준 사람이 선물 받기
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if table[i][j] > table[j][i]:
                answer[i] += 1
            elif table[i][j] < table[j][i]:
                answer[j] += 1
            else:
                if result[i] > result[j]:
                    answer[i] += 1
                elif result[i] < result[j]:
                    answer[j] += 1
    return max(answer)

import sys
f = list(sys.stdin.readline().strip().split('", "'))
g = list(sys.stdin.readline().strip().split('", "'))
print(solution(f, g))