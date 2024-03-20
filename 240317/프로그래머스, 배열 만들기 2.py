# def solution(l, r):
#     answer = []
#     for num in range(l, r+1):
#         if not (set(str(num)) - set(['0', '5'])):
#             answer.append(num)
#     return answer if answer else [-1]

# 이 코드가 더 빠르지만 위의 코드가 간결해 남긴다
def solution(l, r):
    answer = []
    for num in range(l, r+1):
        n = str(num)
        n = n.replace('0', '')
        n = n.replace('5', '')
        if n == '':
            answer.append(num)
    if len(answer) == 0:
        answer.append(-1)
    return answer

import sys

l, r = map(int, sys.stdin.readline().split())
print(solution(l, r))