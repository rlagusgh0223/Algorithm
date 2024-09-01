def solution(number, k):
    answer = []
    for num in number:
        while k>0 and answer and answer[-1]<num:
            answer.pop()
            k -= 1
        answer.append(num)
    return ''.join(answer[:len(answer)-k])

import sys

number = sys.stdin.readline().strip()
k = int(sys.stdin.readline())
print(solution(number, k))