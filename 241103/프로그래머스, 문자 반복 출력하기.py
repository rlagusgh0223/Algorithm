def solution(my_string, n):
    answer = ''
    for m in my_string:
        answer += m*n
    return answer

import sys

m = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
print(solution(m, n))