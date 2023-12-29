def solution(s, n):
    answer = ''
    for S in s:
        if ord('a') <= ord(S) <= ord('z'):
            answer += chr((ord(S)+n-ord('a'))%26 + ord('a'))
        elif ord('A') <= ord(S) <= ord('Z'):
            answer += chr((ord(S)+n-ord('A'))%26 + ord('A'))
        else:
            answer += ' '
    return answer

import sys
s = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
print(solution(s, n))