# code[i] == '1'이면 mode를 바꾼다(0, 1)
# mode가 0일땐 i가 짝수일때만(i%2==0) 문자열 뒤에 붙이고
# mode가 1일땐 i가 홀수일때만(i%2==1) 문자열 뒤에 붙인다

def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode = (mode+1) % 2
        else:
            if i%2 == mode:
                answer += code[i]
    if len(answer) == 0:
        answer = 'EMPTY'
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
