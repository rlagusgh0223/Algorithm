def solution(ability):
    # global 변수로 할 경우 answer를 선언할때 쓰고,
    # 사용할 함수마다 global을 또 써야하기 때문에 줄이 길어지는게 싫어 간단하게 리스트로 만들었다
    answer = [0]
    check = [0] * len(ability)  # DFS를 위해 계산한 학생인지 체크하기 위한 리스트
    
    def DFS(idx, maxSum):  # 종목 번호, 지금까지 점수의 합
        # 모든 종목을 더했다면 최댓값 비교
        if idx == len(ability[0]):
            answer[0] = max(answer[0], maxSum)
            return
        
        # 계산하지 않은 학생의 해당 종목 점수를 추가
        for i in range(len(ability)):
            if check[i] == 0:
                check[i] = 1
                DFS(idx+1, maxSum+ability[i][idx])
                check[i] = 0
    DFS(0, 0)
    return answer[0]


import sys

ability = list(sys.stdin.readline().strip().split("], ["))
ability = [list(map(int, a.split(", "))) for a in ability]
print(solution(ability))