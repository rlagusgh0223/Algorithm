# 1. 각 place별로 P가 있는 위치 파악
# 2. 모든 P의 위치 중 맨해튼거리 구하기 
#   2-1. 1이면 거리두기 안됨(바로 4번 수행)
#   2-2. 2이면 거리두기 확인(3번 수행)
# 3. 맨해튼거리 2인 곳 들의 좌표 사이에 파티션이 없으면 거리두기 안 한다고 체크
# 4. 거리두기를 하고있는지 여부에 따라 1, 0을 answer에 입력

def solution(places):
    answer = []
    for place in places:
        check = []
        ck = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    check.append([i, j])
        
        for x1, y1 in check:
            if not ck:
                break
            for x2, y2 in check:
                if x1==x2 and y1==y2:
                    continue
                dist = abs(x1-x2) + abs(y1-y2)
                if dist == 1:
                    ck = False
                    break
                elif dist == 2:
                    if x1 == x2:
                        if place[x1][(y1+y2)//2] != 'X':
                            ck = False
                            break
                    elif y1 == y2:
                        if place[(x1+x2)//2][y1] != 'X':
                            ck = False
                            break
                    else:
                        if place[x1][y2]!='X' or place[x2][y1]!='X':
                            ck = False
                            break
        if ck:
            answer.append(1)
        else:
            answer.append(0)

    return answer

import sys

places = list(sys.stdin.readline().strip().split('"], ["'))
places = [list(p.split('", "')) for p in places]
print(solution(places))