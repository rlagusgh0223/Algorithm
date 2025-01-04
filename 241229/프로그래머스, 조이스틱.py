def solution(name):
    answer = sum(min(ord(n)-65, 91-ord(n)) for n in name)
    move = len(name)-1
    for standard in range(len(name)):
        nxt = standard+1
        while nxt<len(name) and name[nxt]=='A':
            nxt += 1
        move = min(move, 2*standard + len(name)-nxt, standard + 2*(len(name)-nxt))
    return answer + move

import sys

print(solution(sys.stdin.readline().strip()))
