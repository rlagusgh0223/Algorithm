def solution(edges):
    answer = [0, 0, 0, 0]  # 생성 정점 번호, 도넛, 막대, 8자
    max_edge = max(map(max, edges)) + 1  # edges에서 가장 큰 정점 번호+1
    cnt = [[0, 0] for _ in range(max_edge)]  # 각 정점에서 나가는거, 들어오는거 입력할 리스트

    for a, b in edges:
        cnt[a][0] += 1
        cnt[b][1] += 1

    for i in range(1, max_edge):
        # 나가는거는 2개 이상, 들어오는건 없으면 생성 정점
        if cnt[i][0]>=2 and cnt[i][1]==0:
            answer[0] = i
        # 나가는게 없고, 들어오는게 1개 이상이면
        # 막대그래프의 마지막 정점
        # 그래프의 종류가 몇개인지만 구하면 되므로
        # 막대그래프는 마지막 정점의 개수만 구하면 된다
        elif cnt[i][0]==0 and cnt[i][1]>=1:
            answer[2] += 1
        # 나가는건 2개, 들어오는건 2개 이상이면 8자
        # 8자의 중간지점의 개수만 구하면 된다
        elif cnt[i][0]==2 and cnt[i][1]>=2:
            answer[3] += 1
    # 생성 정점에서 나갔는데, 아직 카운트 되지 않은 그래프의 종류는
    # 도넛 모양 그래프
    answer[1] = cnt[answer[0]][0] - sum(answer[2:])
    return answer

import sys

e = list(sys.stdin.readline().strip().split("], ["))
e = [list(map(int, E.split(', '))) for E in e]
print(solution(e))