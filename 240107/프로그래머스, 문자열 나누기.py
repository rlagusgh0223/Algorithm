# 모범답안
# 원리는 비슷하지만 좀 더 깔끔해서 남긴다
def solution(s):
    answer = 0
    ck1, ck2 = 0, 0
    for now in s:
        if ck1 == ck2:
            answer += 1
            check = now
        if check == now:
            ck1 += 1
        else:
            ck2 += 1
    return answer

def solutions(s):
    answer = 0
    check = ''
    for now in s:
        if check == '':
            check = now
            c, k = 1, 0
        elif now == check:
            c += 1
        else:
            k += 1
        if c == k:
            answer += 1
            check = ''
            c, k = 0, 0
    if c != 0:
        answer += 1
    return answer

import sys
s = sys.stdin.readline().strip()
print(solution(s))