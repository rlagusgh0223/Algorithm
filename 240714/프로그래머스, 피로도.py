from itertools import permutations


def solution(k, dungeons):
    answer = 0
    # dungeons로 나올 수 있는 모든 순서 계산
    dungeons = list(permutations(dungeons, len(dungeons)))
    for dungeon in dungeons:
        now, cnt = k, 0  # 현재 피로도, 탐사한 던전
        for d in dungeon:
            if now >= d[0]:
                now -= d[1]
                cnt += 1
            # 이번 던전을 탐사 못한다면 다음부턴 계산할 필요 없다
            # 모든 순서를 계산하므로 이번 던전 제외하고
            # 다음 던전을 탐사하는건 다른 순서로 입력된 리스트에서 계산한다
            else:
                break
        answer = max(answer, cnt)

    return answer

import sys

k = int(sys.stdin.readline())
dungeons = list(sys.stdin.readline().strip().split("],["))
dungeons = [list(map(int, d.split(","))) for d in dungeons]
print(solution(k, dungeons))