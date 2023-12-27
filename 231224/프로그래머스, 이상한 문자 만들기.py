# 띄어쓰기로 구분하는거 그냥 해도 파이썬에서는 기본적으로 돌아가는데
# 프로그래머스에서는 인정 안되는거 같다
# 띄어쓰기로 리스트 구분할땐 ' '를 spilt()안에 넣어주자
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