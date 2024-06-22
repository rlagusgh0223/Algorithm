def solution(n, results):
    pro = [[0]*n for _ in range(n)]  # 선수들의 승패를 기록할 리스트
    for x, y in results:
        # x는 이긴 사람, y는 진 사람
        # 이긴사람은 1, 진 사람은 -1로 상대방 기록
        pro[x-1][y-1] = 1
        pro[y-1][x-1] = -1
    
    # 플로이드-워셜
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 자기 자신이거나 승패가 이미 난 경우(1 또는 -1)라면 그냥 통과
                if i==j or pro[i][j] in [1, -1]:
                    continue
                # i선수가 k선수를 이기고, k선수가 j선수를 이겼다면
                if pro[i][k] == pro[k][j] == 1:
                    # i선수는 j를 이기고
                    pro[i][j] = 1
                    # j선수는 i와 k에게, k는 i에게 진다
                    pro[j][i] = pro[j][k] = pro[k][i] = -1
    
    # 승패를 알 수 없는 경우가 1번, 즉 자기 자신뿐일 경우
    # 순위를 알 수 있다
    return sum(1 for p in pro if p.count(0)==1)

import sys

n = int(sys.stdin.readline())
results = list(sys.stdin.readline().strip().split("], ["))
results = [list(map(int, r.split(", "))) for r in results]
print(solution(n, results))