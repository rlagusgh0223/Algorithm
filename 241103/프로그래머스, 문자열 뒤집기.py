def solution(my_string):
    # return my_string[::-1]
    return ''.join(list(reversed(my_string)))

import sys

print(solution(sys.stdin.readline().strip()))
