def solution(brown, yellow):
    # brown은 8 이상, yellow는 1 이상이라고 했으므로 9칸(3x3) 이상의 사각형이다
    # brown개수는 4변 중 2변이 같으므로(위아래, 좌우) 절반의 길이만큼 계산하면 된다다
    for i in range(3, brown//2):
        for j in range(3, brown//2):
            # brown이 테두리 벽돌이므로 yellow벽돌은 위아래, 좌우 하나씩을 뺀
            # 직사각형 크기만한 격자가 있어야 한다
            if i*j==brown+yellow and (i-2)*(j-2)==yellow:
                return[j, i]

import sys

b, y = map(int, sys.stdin.readline().split())
print(solution(b, y))