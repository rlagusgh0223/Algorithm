def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]  # 문자열일 경우 리스트로는 이렇게 이어붙이지 못하는것 같다
        check = []
        ck = True
        for j in range(len(s)):
            if s[j]=='(' or s[j]=='[' or s[j]=='{':
                check.append(s[j])
            elif j==0 or len(check)==0:
                ck = False
                break
            elif s[j]==')' and check[-1]=='(':
                del check[-1]
            elif s[j]==']' and check[-1]=='[':
                del check[-1]
            elif s[j]=='}' and check[-1]=='{':
                del check[-1]
        if ck and len(check)==0:
            answer += 1
    return answer

import sys
s = sys.stdin.readline().strip()
print(solution(s))