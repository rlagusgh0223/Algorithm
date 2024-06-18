def solution(name):
    answer = 0  # 총 조이스틱 조작 횟수
    move = len(name)  # 좌우 조작 횟수

    for i in range(len(name)):
        # A에서 원하는 문자로 만들기 위해 움직일 최소 조작 횟수를 구한다
        # Z에서부터 이동하려면 A에서 Z로 한번 이동해야되니까 1 더한다
        answer += min(ord(name[i])-ord('A'), ord('Z')+1-ord(name[i]))

        # 다음 키로 이동 횟수 구하기
        nxt = i+1
        # 연속된 A면 그냥 다음 수로 넘어간다
        while nxt<len(name) and name[nxt]=='A':
            nxt += 1
        # 지금까지 이동횟수 최솟값, 앞으로 갔다가 다시 되돌아오고 뒤로 가는 값,
        # 뒤로 갔다가 다시 돌아오고 앞으로 가는 값 중 가장 작은값 입력
        move = min(move, 2*i+len(name)-nxt, i+2*(len(name)-nxt))
    return answer+move

import sys

print(solution(sys.stdin.readline().strip()))
