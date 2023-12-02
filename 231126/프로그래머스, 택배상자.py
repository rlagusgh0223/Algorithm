def solution(order):
    # 두번째 컨베이어벨트(stack)에는 1,2,3,4,5 이런 순으로 순서대로 쌓인다
    # 하지만 트럭에는 order에 입력된 대로 넣어야 된다
    # 즉, stack의 마지막 값이 order의 순서와 같으면 넣으면 된다
    # 이런식으로 했을때 트럭에 넣을 수 있는 상자의 수
    answer = 0  # order 순서대로 넣을 상자 번호
    stack = []
    for i in range(len(order)):
        stack.append(i+1)
        while stack and stack[-1]==order[answer]:
            answer += 1
            stack.pop()
    return answer

import sys
order = list(map(int, sys.stdin.readline().split(", ")))
print(solution(order))