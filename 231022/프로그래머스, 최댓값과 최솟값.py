def solution(s):
    answer = ''
    check = [int(n) for n in s.split()]
    check.sort()
    answer = str(check[0]) + ' ' + str(check[-1])
    return answer

import sys
s = sys.stdin.readline().rstrip()
print(solution(s))