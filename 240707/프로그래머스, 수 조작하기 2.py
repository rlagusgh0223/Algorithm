def solution(numLog):
    answer = ''
    n = numLog[0]
    for num in numLog[1:]:
        if num == n+1:
            answer += 'w'
            n += 1
        elif num == n-1:
            answer += 's'
            n -= 1
        elif num == n+10:
            answer += 'd'
            n += 10
        elif num == n-10:
            answer += 'a'
            n -= 10
    return answer

import sys

print(solution(list(map(int, sys.stdin.readline().split(", ")))))
