def solution(weights):
    answer = 0
    dic = {}
    for i in weights:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    # 1:1, 2:3, 2:4, 3:4의 비율이면 짝꿍이 된다
    for i in dic:
        # 중복된 값이 있을 경우(1:1) 그 값들끼리 연결했을때 나오는 경우의 수를 더한다
        if dic[i] > 1:
            answer += (dic[i] * (dic[i]-1)) // 2
        # 2:3, 3:4, 4:2의 비율인 경우
        # 3:2, 4:3, 2:4 처럼 비율이 반대인 경우는 나중에 반대편 수가 계산할때 체크될거다
        # 코드에서는 기억하기 쉽게 2:3, 3:4, 4:2로 반영했다
        if i*2/3 in dic:
            answer += dic[i] * dic[i*2/3]
        if i*3/4 in dic:
            answer += dic[i] * dic[i*3/4]
        if i*4/2 in dic:
            answer += dic[i] * dic[i*4/2]
    return answer

import sys
w = list(map(int, sys.stdin.readline().split(",")))
print(solution(w))