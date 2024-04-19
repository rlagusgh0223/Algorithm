def solution(arr):
    # 영역은 0과 1로 이루어져 있으므로 두 영역의 개수를 입력할 리스트 생성
    answer = [0, 0]

    def quard(x, y, l):
        # 현재 위치를 기준으로 주변에 같은 영역인지 확인
        now = arr[x][y]
        for i in range(x, x+l):
            for j in range(y, y+l):
                # 다른 영역이 나온다면 영역의 길이를 반으로 줄이고
                # 새롭게 영역을 탐색한다
                if now != arr[i][j]:
                    l = l//2
                    quard(x, y, l)
                    quard(x+l, y, l)
                    quard(x, y+l, l)
                    quard(x+l, y+l, l)
                    return
        # 위에서 리턴되지 않았다면 정사각형으로 영역이 채워진 것이므로
        # 영역의 수 더한다
        answer[now] += 1
    quard(0, 0, len(arr))
    return answer

import sys

arr = list(sys.stdin.readline().strip().split("],["))
arr = [list(map(int, a.split(","))) for a in arr]
print(solution(arr))