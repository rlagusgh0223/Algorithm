# replace : 문자열을 변경하는 함수
# replace(현재 문자열에서 변경하고 싶은 문자, 새로 바꿀 문자, 변경할 횟수[없으면 모든 문자열 변경])
# 모범답안
def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        s = s.replace(num[i], str(i))
    return int(s)

import sys
s = sys.stdin.readline().strip()
print(solution(s))

# 내 풀이
def solutions(s):
    answer = ''
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    word = ''
    for S in s:
        if word in num:
            answer += str(num.index(word))
            word = ''
        if ord('0') <= ord(S) <= ord('9'):
            answer += S
        else:
            word += S
    if word:
        answer += str(num.index(word))
    return int(answer)