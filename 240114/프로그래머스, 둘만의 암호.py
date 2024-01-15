# 다른 방법
# ascii_lowercase는 알파벳 소문자를 가져온다
from string import ascii_lowercase
def solution(s, skip, index):
    answer = ''
    word = list(ascii_lowercase)
    for now in skip:
        # remove를 이용하면 리스트 안에서 해당하는 첫번째 값을 지운다
        word.remove(now)
    for now in s:
        answer += word[(word.index(now)+index)%len(word)]
    return answer


def solutions(s, skip, index):
    answer = ''
    for now in s:
        ck = 0
        while ck<index:
            now = chr((ord(now) - ord('a')+1)%26 + ord('a'))
            if now not in skip:
                ck += 1
        answer += now
    return answer

import sys
s = sys.stdin.readline().strip()
skip = sys.stdin.readline().strip()
index = int(sys.stdin.readline())
print(solution(s, skip, index))