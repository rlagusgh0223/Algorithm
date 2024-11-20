def solution(my_string):
    return my_string.swapcase()
    # answer = ''
    # for s in my_string:
    #     if s.isupper():
    #         answer += s.lower()
    #     else:
    #         answer += s.upper()
    # return answer

import sys

print(solution(sys.stdin.readline()))
