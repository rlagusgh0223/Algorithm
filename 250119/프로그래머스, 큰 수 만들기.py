def solution(number, k):
    answer = []
    for num in number:
        while k>0 and answer and answer[-1]<num:
            k -= 1
            answer.pop()
        answer.append(num)
    # 98765같은 앞의 숫자가 더 큰 문자열은 k가 0이 아닐 수 있다
    # 그러므로 마지막에 남아있는 k만큼 뒤의 문자열에서 빼준다
    return ''.join(answer[:len(number)-k])

import sys

number = sys.stdin.readline().strip()
k = int(sys.stdin.readline())
print(solution(number, k))