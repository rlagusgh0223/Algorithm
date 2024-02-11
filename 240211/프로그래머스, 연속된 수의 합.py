def solution(num, total):
    answer = []
    # 연속된 수의 첫 번째 계산
    start = (total//num) - ((num-1)//2)
    for i in range(num):
        answer.append(start+i)
    return answer


import sys

num, total = map(int, sys.stdin.readline().split())
print(solution(num, total))