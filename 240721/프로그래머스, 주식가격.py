# 주어진 리스트에 해당 값보다 작은값이 뒤에 나오거나
# 리스트가 끝나는 지점까지 걸리는 시간을 반환하면 된다
def solution(prices):
    # 시간을 저장할 리스트
    # 뒤에 자기보다 작은 값이 없다는 가정하에
    # 끝까지 갔을때의 시간으로 초기화 한다
    answer = [i for i in range(len(prices)-1, -1, -1)]

    # 뒤의 값과 비교하기 위한 값의 인덱스를 저장할 스택
    stack = [0]
    
    # 모든 값을 비교한다(0번째는 이미 값을 넣었으므로 1번째부터 시작한다)
    for i in range(1, len(prices)):
        # stack에 값이 있고 지금 값(i)보다 값이 크다면 
        # 스택에서 빼고 지금까지 걸린 시간을 answer에 입력한다
        # 스택에 값이 없거나 지금 값 보다 작은 값이 나올때까지 반복한다
        while stack and prices[stack[-1]] > prices[i]:
            now = stack.pop()  # 스택에서 인덱스를 받아온다
            answer[now] = i - now  # 현재 시간 - 인덱스(인덱스부터 작은값이 나올때까지 시간)을 answer에 입력한다
        
        # 현재 값의 앞의 값들과는 비교 끝났고
        # 지금 값을 스택에 입력하여 뒤의 값들과 비교하게 한다
        stack.append(i)
    return answer

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
