def solution(n):
    answer = n
    # bin으로 작성한 2진수는 따로 문자열로 바꾸지 않아도 문자로 카운트 되는것 같다
    check = bin(n).count('1')
    while True:
        answer += 1
        if check == bin(answer).count('1'):
            return answer

import sys
n = int(sys.stdin.readline())
print(solution(n))