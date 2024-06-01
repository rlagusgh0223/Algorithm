from itertools import permutations


def solution(n, weak, dist):
    answer = []
    # 한 바퀴 돈 이후에도 약한 부분을 리스트에 입력
    weaks = weak + [w+n for w in weak]
    
    # 각 취약점에서 전부 시작
    for i in range(len(weak)):
        # 현재 친구들이 점검하는 모든 경우의 수로 계산
        for friend in permutations(dist):
            cnt = 1  # 필요한 친구 수
            now = weak[i]  # 지금 있는 취약점 위치
            for f in friend:
                now += f
                # 지금 위치가 점검 가능한 모든곳을 점검하고 다시 자기한테 가기 전이라면
                # 갈 수 있는 만큼 가고 그 다음 취약점을 현재위치로 바꾸고 친구를 한명 추가한다
                # 거긴 새 친구가 검사할거다
                if now < weaks[i+len(weak)-1]:
                    cnt += 1
                    now = [w for w in weaks[i+1:i+len(weak)] if w>now][0]
                # 끝까지 갔다면 친구가 그만큼만 필요하므로
                # 필요한 친구 수를 리스트에 입력하고 이번 계산 종료
                else:
                    answer.append(cnt)
                    break
    # 필요한 친구 수 중 가장 적은 인원을 리턴하거나
    # 친구들이 모두 점검할 수 없으면 -1 리턴
    return min(answer) if answer else -1

import sys

n = int(sys.stdin.readline())
weak = list(map(int, sys.stdin.readline().split(", ")))
dist = list(map(int, sys.stdin.readline().split(", ")))
print(solution(n, weak, dist))