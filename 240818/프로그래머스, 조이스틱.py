def solution(name):
    answer = sum(min(ord(n)-ord('A'), ord('Z')+1-ord(n)) for n in name)
    move = len(name) - 1
    for i in range(len(name)):
        nxt = i+1
        while nxt<len(name) and name[nxt]=='A':
            nxt += 1
        move = min(move, 2*i + len(name)-nxt, i + 2*(len(name)-nxt))
    return answer + move

import sys

print(solution(sys.stdin.readline().strip()))


