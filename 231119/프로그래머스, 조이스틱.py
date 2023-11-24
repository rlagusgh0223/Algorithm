def solution(name):
    answer = 0
    move = len(name) - 1
    for i in range(len(name)):
        answer += min(ord(name[i])-ord('A'), ord('Z')+1-ord(name[i]))
        nxt = i+1
        while nxt<len(name) and name[nxt]=='A':
            nxt += 1
        move = min(move, 2*i+len(name)-nxt, i+2*(len(name)-nxt))
    answer += move
    return answer

import sys
name = sys.stdin.readline().strip()
print(solution(name))