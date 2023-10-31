# 모범답안
def solutions(n, words):
    for w in range(1, len(words)):
        if words[w][0]!=words[w-1][-1] or words[w] in words[:w]:
            return [(w%n)+1, (w//n)+1]
    else:
        return [0, 0]

def solution(n, words):
    cnt, ck = 1, 0
    people, check = [], []
    for now in words:
        ck += 1
        if len(check)!=0 and check[-1]!=now[0]:
            return [ck, cnt]
        elif now in people:
            return [ck, cnt]
        else:
            people.append(now)
            check = list(now)
        if ck == n:
            ck = 0
            cnt += 1
    return [0, 0]

import sys
n = int(sys.stdin.readline())
words = list(sys.stdin.readline().split())
print(solution(n, words))