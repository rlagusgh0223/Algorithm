answer = 0

def DFS(idx, maxSum, check, ability):
    global answer
    if idx == len(ability[0]):  # 모든 과목수만큼 더했다면 최댓값 비교
        answer = max(answer, maxSum)
    else:
        for i in range(len(ability)):  # 모든 사람들을 비교하기 위한 반복문
            if check[i] == 0:  # 이번 사람을 계산하지 않았다면 계산에 추가
                check[i] = 1
                DFS(idx+1, maxSum+ability[i][idx], check, ability)
                check[i] = 0

def solution(ability):
    global answer
    check = [0] * len(ability)  # 어떤 학생이 계산에 들어왔는지 표시하기 위한 리스트
    DFS(0, 0, check, ability)
    return answer

import sys

ability = list(sys.stdin.readline().strip().split("], ["))
ability = [list(map(int, a.split(", "))) for a in ability]
print(solution(ability))