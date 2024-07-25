def solution(tickets):
    answer = []
    # 모든 항공권을 이용한다고 했으므로 모든 티켓을 써야 한다
    # 모든 티켓을 사용했는지 체크하는 리스트
    check = [0] * len(tickets)

    # 출발하려는 공항, 지금까지 방문한 경로
    def DFS(start, visit):
        # 모든 티켓을 다 쓰면 방문한 공항은 티켓의 수보다 1 더 많아야 하므로 
        # 방문한 공항의 수가 티켓의 수 + 1이 되면 해당 경로를 answer에 입력한다
        if len(visit) == len(tickets)+1:
            answer.append(visit)
            return
        
        for idx, ticket in enumerate(tickets):
            # 티켓의 출발지가 해당 공항이고, 티켓을 사용한 적이 없다면
            if ticket[0]==start and check[idx]==0:
                check[idx] = 1
                DFS(ticket[1], visit+[ticket[1]])  # 도착지를 기준으로 DFS를 돌린다
                check[idx] = 0
    DFS("ICN", ["ICN"])
    answer.sort()  # 알파벳 순서가 앞서는 경로가 앞에 오도록 정렬한다
    return answer[0]

import sys

tickets = list(sys.stdin.readline().strip().split('"], ["'))
tickets = [list(t.split('", "')) for t in tickets]
print(solution(tickets))