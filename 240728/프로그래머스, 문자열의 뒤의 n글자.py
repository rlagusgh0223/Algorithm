def solution(my_string, n):
    return my_string[-n:]

import sys

my_string = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
print(solution(my_string, n))