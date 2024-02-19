# 플로이드 - 워셜 문제
def solution(n, results):
    answer = 0
    board = [[0]*n for _ in range(n)]

    # 이긴사람은 1, 진 사람은 -1로 표시
    for a, b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 본인이거나 이미 승부가 났다면 넘어감
                if i==j or board[i][j] in [1, -1]:
                    continue
                # i가 k을 이기고 k가 j를 이겼다면
                if board[i][k] == board[k][j] == 1:
                    # i는 j를 이긴다
                    board[i][j] = 1
                    # j는 i와 k에게, k는 i에게 진다
                    board[j][i] = board[j][k] = board[k][i] = -1
    
    for now in board:
        # 0은 승부를 알 수 없는 사람인데,
        # 1개만 있다면 자신을 제외한 모두와 승부가 난 것이므로
        # 순위를 매길 수 있다
        if now.count(0) == 1:
            answer += 1
    return answer


import sys

n = int(sys.stdin.readline())
results = list(sys.stdin.readline().strip().split("], ["))
results = [list(map(int, result.split(", "))) for result in results]
print(solution(n, results))