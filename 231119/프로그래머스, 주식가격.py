# 모범답안
def solution(prices):
    # 끝까지 지금값보다 작은값이 없을경우 배열 길이 역순의 값으로 출력한다
    answer = [i for i in range(len(prices)-1, -1, -1)]
    stack = [0]  # prices의 위치값을 저장하는 스택
    for now in range(1, len(prices)):
        # 이전값 중 지금값보다 큰 값이 있다면 이전값 중 지금값보다 작은값이 나올때까지
        while stack and prices[stack[-1]] > prices[now]:
            # 확인이 필요한 이전값을 빼고
            before = stack.pop()
            # 이전값의 범위는 여기까지 이므로 지금위치-이전위치 값을 입력한다
            answer[before] = now - before
        stack.append(now)
    return answer

def solutions(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        sec = 0
        for j in range(i+1, len(prices)):
            sec += 1
            if prices[i] > prices[j]:
                break
        answer[i] = sec
    return answer

import sys
prices = list(map(int, sys.stdin.readline().split(", ")))
print(solution(prices))