child = ["RR", "Rr", "Rr", "rr"]
def back(gen, x):
    # 1세대, 최초일 경우 Rr이므로 리턴
    if gen == 1:
        return "Rr"
    # 부모세대에서 몇번째 개체인지는 현재 개체//4를 해야된다
    # 그림 기준으로 3세대 5번개체(RR)일 경우
    # 2세대 1번개체가 부모다
    parent = back(gen-1, x//4)
    # Rr이면 child에서 x%4번째의 완두콩이 자식 완두콩이다
    if parent == 'Rr':
        return child[x%4]
    # 여기까지 왔다는건 부모 완두콩이 RR이나 rr이라는건데
    # 모든 자식들은 부모와 동일하므로 그대로 리턴
    return parent

def solution(queries):
    answer = []
    # 각 쿼리의 개체를 확인 후 answer에 입력
    for n, p in queries:
        # 각 세대(n)의 개체(p-1)의 값 구하기
        # 처음 p입력했을때보다 1 적은 값을 입력해야 구할 수 있다
        # p는 1을 시작으로 입력하는데 계산은 0을 시작으로 해야되기 때문이다
        result = back(n, p-1)
        answer.append(result)
    return answer

import sys

queries = list(sys.stdin.readline().strip().split("], ["))
queries = [list(map(int, q.split(", "))) for q in queries]
print(solution(queries))