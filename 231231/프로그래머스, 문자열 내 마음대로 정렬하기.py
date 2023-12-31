def solution(strings, n):
    strings.sort()
    return sorted(strings, key = lambda x:x[n])

import sys
strings = list(sys.stdin.readline().strip().split('", "'))
n = int(sys.stdin.readline())
print(solution(strings, n))