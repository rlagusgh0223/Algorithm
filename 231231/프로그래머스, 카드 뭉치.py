def solution(cards1, cards2, goal):
    for g in goal:
        if cards1 and cards1[0] == g:
            del cards1[0]
        elif cards2 and cards2[0] == g:
            del cards2[0]
        else:
            return "No"
    return "Yes"

import sys
cards1 = list(sys.stdin.readline().strip().split('", "'))
cards2 = list(sys.stdin.readline().strip().split('", "'))
goal = list(sys.stdin.readline().strip().split('", "'))
print(solution(cards1, cards2, goal))