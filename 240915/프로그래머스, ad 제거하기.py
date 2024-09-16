def solution(strArr):
    return [arr for arr in strArr if 'ad' not in arr]

import sys

print(solution(list(sys.stdin.readline().strip().split('","'))))
