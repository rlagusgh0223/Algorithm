child = ['RR', 'Rr', 'Rr', 'rr']
def back(g, q):
    # 1세대가 입력되면 하나뿐이므로 바로 Rr을 리턴한다
    if g == 1:
        return 'Rr'
    
    # 부모 세대는 어떤 개체인지 확인한다
    # 모든 부모는 4개의 자식 개체를 만드므로
    # 4로 나눈 몫이 부모의 개체 번호가 된다
    parent = back(g-1, q//4)

    # 부모가 잡종 개체일 경우 child의 형태 중 하나가 된다
    if parent == 'Rr':
        return child[q%4]
    
    # 부모가 순종 개체면 부모의 순종을 그대로 따른다
    return parent

def solution(queries):
    answer = []
    for g, q in queries:  # 세대(g), 개체번호(q)
        # 개체번호는 //와 %연산을 해야하므로 0에서부터 시작해야된다
        # q는 1부터 시작하는걸 가정하여 줬으므로 1을 빼고 입력한다
        answer.append(back(g, q-1))
    return answer

import sys

queries = list(sys.stdin.readline().strip().split("], ["))
queries = [list(map(int, q.split(", "))) for q in queries]
print(solution(queries))