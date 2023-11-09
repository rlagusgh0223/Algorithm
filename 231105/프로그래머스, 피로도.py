def solution(k, dungeons):
    answer = 0
    # 순서에 상관 없이 가능한 모든 경우의 수를 d에 입력한다
    d = list(permutations(dungeons, len(dungeons)))
    for now in d:
        nk, ck = k, 0  # 남은 피로도, 지나온 던전
        for n in now:
            # 남은 피로도로 던전에 들어갈 수 있으면 들어간 후 소모 피로도를 제하고, 던전 탐험 횟수를 1 증가한다
            if nk >= n[0]:
                nk -= n[1]
                ck += 1
        answer = max(answer, ck)
    return answer



from itertools import permutations
import sys
k = int(sys.stdin.readline())
dun = sys.stdin.readline().strip().split("],[")
dungeons = []
for d in dun:
    d = list(map(int, d.split(',')))
    dungeons.append(d)
print(solution(k, dungeons))