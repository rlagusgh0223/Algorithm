def solution(s):
    answer = ''
    for now in range(len(s)):
        # 공백이 여러칸 주어지면 그 공백을 다 반영해야 된다
        if s[now] == ' ':
            answer += ' '
        else:
            if (now==0) or (now>0 and s[now-1]==' '):
                answer += s[now].upper()
            else:
                answer += s[now].lower()
    return answer

import sys
s = sys.stdin.readline().rstrip()
print(solution(s))