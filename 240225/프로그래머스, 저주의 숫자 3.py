def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer%3==0 or '3' in str(answer):
            answer += 1
    return answer

# def solution(n):
#     answer = [i for i in range(300) if (i%3!=0 and '3' not in str(i))]
#     return answer[n-1]


import sys

print(solution(int(sys.stdin.readline())))
