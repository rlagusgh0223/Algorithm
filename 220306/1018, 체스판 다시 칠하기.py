# 상하좌우로 현재 칸과 다른 색이 나와야 되는데 그건 어떻게 계산되는건지 모르겠다....
import sys
n, m = map(int, sys.stdin.readline().split())
ground = [0 for _ in range(n)]    # 입력받은 체스판
count = []    # 바뀐 체스판

for i in range(n):
    ground[i] = list(sys.stdin.readline())

for a in range(n-7):    # 체스판에서 시작점을 잡기 위한 반복문
    for b in range(m-7):    # 체스판을 만들 수 있는 위치에서 시작 range(n-7)이니까 n-8까지 시작점이 될 수 있다(체스판은 8칸)
        index1 = 0    # 'W'로 시작할 경우 체스판의 갯수를 세는 변수
        index2 = 0    # 'B'로 시작할 경우 체스판의 갯수를 세는 변수
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2 == 0:    # 짝수칸이므로 시작점의 색깔과 같아야 한다
                    if ground[i][j] != 'W':    # 'W'로 시작했는데 'W'가 아닌 경우
                        index1 += 1
                    if ground[i][j] != 'B':    # 'B'로 시작했는데 'B'가 아닌 경우
                        index2 += 1
                else:    # 홀수칸이므로 시작점의 색깔과 달라야 한다
                    if ground[i][j] != 'B':    # 'W'로 시작했으니까 'B'가 와야되는데 'B'가 아닌 경우
                        index1 += 1
                    if ground[i][j] != 'W':    # 'B'로 시작했으니까 'W'가 와야되는데 'W'가 아닌 경우
                        index2 += 1
        
        # 'W'로 시작할 경우와 'B'로 시작할 경우 바뀐 체스판의 수 중 작은 수를 count리스트에 추가
        count.append(min(index1, index2))

print(min(count))