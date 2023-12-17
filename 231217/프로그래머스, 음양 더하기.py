def solution(absolutes, signs):
    answer = 0
    for s in range(len(signs)):
        if signs[s] == False:
            answer += (-1 * absolutes[s])
        else:
            answer += absolutes[s]
    return answer


import sys
absolutes = list(map(int, sys.stdin.readline().strip().split(",")))
signs = list(sys.stdin.readline().strip().split(","))
print(solution(absolutes, signs))