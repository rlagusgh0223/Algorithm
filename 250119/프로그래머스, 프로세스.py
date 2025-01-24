def solution(priorities, location):
    answer = 0
    stack = list(enumerate(priorities))
    while True:
        now = stack.pop(0)
        # any()
        # 반복 가능한 객체에서 하나 이상의 요소가 참인지 검사
        # 하나라도 조건을 만족하면 True 반환환
        if any(now[1]<s[1] for s in stack):
            stack.append(now)
        else:
            answer += 1
            if now[0] == location:
                return answer

import sys

p = list(map(int, sys.stdin.readline().split(", ")))
l = int(sys.stdin.readline())
print(solution(p, l))