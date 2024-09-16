def solution(strArr):
    answer = [arr for arr in strArr if 'ad' not in arr]
    return answer

import sys

print(solution(list(sys.stdin.readline().strip().split('","'))))
