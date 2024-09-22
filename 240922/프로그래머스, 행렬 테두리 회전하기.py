# 1. 주어진 값 중 x1y1 x2y2값을 반복문으로 받는다
# 2. [x1][y1]->[x1][y2], [x1][y2]->[x2][y2], [x2][y2]->[x2][y1], [x2][y1]->[x1][y1]으로 값을 바꾼다
# 3. 값을 넘기는 과정에서 가장 작은 값을 구한 후 answer에 입력한다

# 이를 위해 앞의 값을 저장할 변수(ck)와 가장 작은 값을 저장할 변수(minq) 두개가 필요하다


def solution(rows, columns, queries):
    answer = []
    ground = [[0]*(columns+1) for _ in range(rows+1)]
    ck = 1
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            ground[i][j] = ck
            ck += 1

    for x1, y1, x2, y2 in queries:
        minq = ck = ground[x1][y1]
        # [x1][y1]->[x1][y2]
        for y in range(y1+1, y2):
            ck, ground[x1][y] = ground[x1][y], ck
            minq = min(minq, ck)
        
        # [x1][y2]->[x2][y2]
        for x in range(x1, x2):
            ck, ground[x][y2] = ground[x][y2], ck
            minq = min(minq, ck)

        # [x2][y2]->[x2][y1], 
        for y in range(y2, y1, -1):
            ck, ground[x2][y] = ground[x2][y], ck
            minq = min(minq, ck)
            
        # [x2][y1]->[x1][y1]
        for x in range(x2, x1, -1):
            ck, ground[x][y1] = ground[x][y1], ck
            minq = min(minq, ck)
        ck, ground[x1][y1] = ground[x1][y1], ck
        minq = min(minq, ck)
        
        answer.append(minq)
    return answer


import sys

rows, columns = map(int, sys.stdin.readline().split())
queries = list(sys.stdin.readline().strip().split("],["))
queries = [list(map(int, q.split(","))) for q in queries]
print(solution(rows, columns, queries))