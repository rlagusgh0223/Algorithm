def solution(N, stages):
    answer = {}
    ls = len(stages)
    for i in range(1, N+1):
        if ls == 0:
            answer[i] = 0
        else:
            cnt = stages.count(i)
            answer[i] = cnt/ls
            ls -= cnt
    # key=lambda x:answer[x]
    # : answer[x]의 x는 key를 의미하므로 answer의 value을 기준으로 정렬한다는 뜻
    return sorted(answer, key=lambda x:answer[x], reverse=True)


import sys
n = int(sys.stdin.readline())
stages = list(map(int, sys.stdin.readline().strip().split(", ")))
print(solution(n, stages))