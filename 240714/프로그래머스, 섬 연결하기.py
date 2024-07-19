def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])  # 비용이 적은 다리부터 오름차순 정렬
    island = set([costs[0][0]])  # 연결된 섬들을 저장할 집합. 맨 처음 섬을 입력한다

    # 모든 섬이 연결될 때까지 반복
    while len(island) < n:
        for c in costs:
            # XOR연산자를 이용하여 둘 중 하나의 섬만 기존에 연결되어 있던 경우 새로운 섬을 연결한다
            if (c[0] in island) ^ (c[1] in island):
                # add는 하나하나 입력해야 하지만
                # update는 요소 안의 모든 값들을 집합에 저장한다
                island.update([c[0], c[1]])
                answer += c[2]  # 다리 통행료를 더한다
                break  # 새로운 간선 찾았으므로 루프 탈출하여 다시 시작한다
    return answer

import sys

n = int(sys.stdin.readline())
costs = list(sys.stdin.readline().strip().split("],["))
costs = [list(map(int, c.split(","))) for c in costs]
print(solution(n, costs))