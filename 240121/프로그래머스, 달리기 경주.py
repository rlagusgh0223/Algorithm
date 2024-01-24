def solution(players, callings):
    # callings의 최대 길이가 1000000이고 players의 최대 길이가 50000이라
    # players.index()를 이용하면 시간초과 나온다
    # answer는 각 플레이어의 위치를 저장하는 딕셔너리다
    answer = {palyer:i for i, palyer in enumerate(players)}
    for call in callings:
        # 현재 말하는 사람의 위치 찾는다
        idx = answer[call]
        # 그 번호의 앞 사람과 위치 바꾼다
        players[idx], players[idx-1] = players[idx-1], players[idx]
        # 위치 바꾼 순서를 answer에 입력한다
        answer[players[idx]] = idx
        answer[players[idx-1]] = idx - 1
    return players

import sys
p = list(sys.stdin.readline().strip().split('", "'))
c = list(sys.stdin.readline().strip().split('", "'))
print(solution(p, c))