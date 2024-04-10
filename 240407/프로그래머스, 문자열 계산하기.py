def solution(my_string):
    # eval() : 문자열로 받은 수식을 계산해 준다
    return eval(my_string)

def solutions(my_string):
    s = my_string.split()
    answer = int(s[0])
    # 예제에는 3 + 4만 있지만
    # 3 + 4 + 5 - 2 이런식으로 여러개의 식이 있을 수 있다
    for i in range(1, len(s), 2):
        if s[i] == '+':
            answer += int(s[i+1])
        else:
            answer -= int(s[i+1])
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
