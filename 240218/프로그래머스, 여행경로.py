def solution(tickets):
    answer = []
    visit = [0] * len(tickets)

    def dfs(airport, path):
        # ticket 하나에 공항 2개니까 모든 공항의 수는 len(tickets)+1
        if len(path) == len(tickets)+1:
            answer.append(path)
            return
        
        for idx, ticket in enumerate(tickets):
            # 출발하는 공항이 현재 공항이고 방문지가 방문한적 없는 곳이라면
            if ticket[0]==airport and visit[idx]==0:
                # 방문한걸로 표시하고 BFS돌린다
                # BFS 끝나고 돌아오면 다시 방문하지 않은걸로 표시
                visit[idx] = 1
                dfs(ticket[1], path+[ticket[1]])
                visit[idx] = 0

    dfs("ICN", ["ICN"])
    
    # answer에는 방문 가능한 모든 경우의 수가 있는데 그 중 알파벳 순으로 앞서는 경로를 정렬한다
    answer.sort()
    return answer[0]

import sys

tickets = list(sys.stdin.readline().strip().split('"], ["'))
tickets = [list(now.split('", "'))for now in tickets]
print(solution(tickets))