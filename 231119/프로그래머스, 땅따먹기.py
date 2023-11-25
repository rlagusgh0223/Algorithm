def solution(land):
    for i in range(1, len(land)):
        # N행 4열
        for j in range(4):
            # 이전 행에서 이번 열을 제외한 리스트를 만들고, 그 중에 가장 큰값을
            # 이번 행 이번 열의 값이랑 더한다
            # 그러면 각 좌표에는 그 자리까지 더할 수 있는 최댓값이 들어온다
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[-1])

import sys
land = list(sys.stdin.readline().strip().split("],["))
land = [list(map(int, land[i].split(","))) for i in range(len(land))]
print(solution(land))