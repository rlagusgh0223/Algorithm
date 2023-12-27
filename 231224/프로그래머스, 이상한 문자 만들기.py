# split()으로만 하면 여러개의 공백이 하나로 들어간다
# split(' ')로 해야 각 공백마다 구분해준다
def solution(s):
    answer = ''
    s = list(s.split(' '))
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j%2 == 0:
                answer += s[i][j].upper()
            else:
                answer += s[i][j].lower()
        if i < len(s) - 1:
            answer += ' '
    return answer


import sys
s = sys.stdin.readline().strip()
print(solution(s))