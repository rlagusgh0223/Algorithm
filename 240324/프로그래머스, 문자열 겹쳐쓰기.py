def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]

import sys

my_string = sys.stdin.readline().strip()
overwrite_string = sys.stdin.readline().strip()
s = int(sys.stdin.readline())
print(solution(my_string, overwrite_string, s))