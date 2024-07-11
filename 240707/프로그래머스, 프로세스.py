def solution(priorities, location):
    # location과 비교할 수 있도록 각 번호에
    # 인덱스도 붙여서 스택을 만든다
    stack = [[x, y] for x, y in enumerate(priorities)]
    answer = 0
    while True:
        # 맨 앞의 스택을 빼서 확인한다
        now = stack.pop(0)
        # any()
        # 반복 가능한 객체에서 하나 이상의 요소가 참인지 검사
        # 하나라도 조건을 만족하면 True 반환
        if any(now[1]<s[1] for s in stack):
            # 하나라도 스택에 큰게 있다면 다시 스택에 넣는다
            stack.append(now)
        else:
            # 지금 꺼낸 값보다 큰 값이 스택에 하나도 없다면
            # 해당 수를 스택에서 제외하고 실행 횟수 증가한다
            answer += 1
            # 이번 수의 인덱스가 location이라면
            # 총 실행 횟수 반환한다
            if now[0] == location:
                return answer


import sys

priorities = list(map(int, sys.stdin.readline().split(", ")))
location = int(sys.stdin.readline)
print(solution(priorities, location))