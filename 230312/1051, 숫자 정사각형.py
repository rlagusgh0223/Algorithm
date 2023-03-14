import sys
N, M = map(int, sys.stdin.readline().split())
rect = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
ck = min(N, M)  # 정사각형의 길이는 짧은 길이보다 길 수 없으므로 짧은 길이의 변을 최대값으로 지정한다
ans = 0  # 최대 정사각형을 비교하기 위한 변수
for i in range(N):
    for j in range(M): # 모든 위치를 검색
        for k in range(ck): # 0~한 변의 최대 길이 만큼
            # 현재 위치에서 k만큼 더 길어져도 사각형 안에 위치하며, 모든 꼭지점의 수가 같다면
            if i+k<N and j+k<M and rect[i][j]==rect[i+k][j]==rect[i][j+k]==rect[i+k][j+k]:
                ans = max(ans, (k+1)**2)  # 지금까지 정사각형 중 최대크기와 지금 정사각형의 크기 중 큰 값을 입력한다(k는 0부터 시작하므로 1 더해줘야 된다)
print(ans)