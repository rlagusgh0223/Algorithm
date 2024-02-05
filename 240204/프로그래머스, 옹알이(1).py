def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for w in word:
            while w in bab:
                bab = bab.replace(w, ' ')
        bab = ''.join(bab.split())
        if bab =='':
            answer += 1
    return answer

import sys
bab = list(sys.stdin.readline().strip().split('", "'))
print(solution(bab))