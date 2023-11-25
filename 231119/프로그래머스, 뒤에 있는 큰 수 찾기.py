def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []  # 뒷 큰수가 있는지 확인할 수의 순서가 입력될 스택
    for i in range(len(numbers)):
        # 뒷 큰수가 있는지 확인하려는 수 들 중에 지금수보다 작은게 있다면
        # 스택에서 지우고 answer에 뒷 큰수를 넣는다
        # 스택에는 앞으로 갈수록 큰 수의 위치만 남는다
        # 스택에 입력하기 전에 뒷 큰수를 비교해보고 지금 수 보다 큰 수만 남기 때문이다
        while stack and numbers[stack[-1]]<numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer

import sys
numbers = list(map(int, sys.stdin.readline().split(", ")))
print(solution(numbers))