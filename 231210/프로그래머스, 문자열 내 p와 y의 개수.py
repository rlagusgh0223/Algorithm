def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False

import sys
s = sys.stdin.readline().strip()
print(solution(s))