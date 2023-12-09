# kruskal 알고리즘
# 탐욕적인 방법을 이용하여 네트워크
# (가중치를 간선에 할당한 그래프)의
# 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 것
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    # 섬에 다리를 연결했는지 확인하기 위한 set에 출발값 입력
    check = set([costs[0][0]])
    while len(check) < n:
        for c in costs:
            # 두 섬 모두 다리가 연결되어 있으면 다음
            if c[0] in check and c[1] in check:
                continue
            # 두 섬 중 한 섬이라고 다리가 연결이 안 되어 있으면
            # 다리를 연결하고 유지비용을 낸다
            if c[0] in check or c[1] in check:
                check.update([c[0], c[1]])
                answer += c[2]
                break
    return answer



import sys
n = int(sys.stdin.readline())
costs = list(sys.stdin.readline().strip().split("],["))
costs = [list(map(int, c.split(","))) for c in costs]
print(solution(n, costs))