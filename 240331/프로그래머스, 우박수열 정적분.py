def solution(k, ranges):
    answer = []
    check = [0.0]

    while k != 1:
        # 우박 수열
        # 주어진 수가 짝수라면, 2로 나눈다
        if k%2 == 0:
            newK = k//2
        # 주어진 수가 홀수라면, 3을 곱하고 1을 더한다
        else:
            newK = k*3 + 1

        # 정적분 넓이
        minY, maxY = min(k, newK), max(k, newK)
        check.append(check[-1] + (minY+(1/2) * (maxY-minY)))
        
        # 자연수 k 갱신
        k = newK

    # 그래프 길이
    N = len(check)
    for y1, y2 in ranges:
        # 정적분이 유효한 구간
        if N + (y2-1) >= y1:
            answer.append(check[y2-1] - check[y1])
        # 시작점이 끝점보다 커서 유효하지 않은 구간
        else:
            answer.append(-1.0)
    return answer

import sys

k = int(sys.stdin.readline())
ranges = list(sys.stdin.readline().strip().split("],["))
ranges = [list(map(int, r.split(","))) for r in ranges]
print(solution(k, ranges))