def solution(brown, yellow):
    # brown은 8이상, yellow는 1이상이라고 했으므로
    # 3x3 이상의 사각형이다
    # brown개수는 4변중 2변이 같으므로(위아래, 좌우)
    # 절반의 길이만큼 계산해보면 된다
    for i in range(3, brown//2):
        for j in range(3, brown//2):
            # brown이 테두리 벽돌이므로 yellow는 위아래,
            # 좌우 각 하나씩을 뺀 변의 직사각형 길이만한
            # 격자 개수가 있어야 한다
            if i*j==brown+yellow and (i-2)*(j-2)==yellow:
                return [j, i]

import sys

brown, yellow = map(int, sys.stdin.readline().split())
print(solution(brown, yellow))