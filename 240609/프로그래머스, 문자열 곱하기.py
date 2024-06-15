def solution(my_string, k):
    return my_string * k

import sys

my_string = sys.stdin.readline().strip()
k = int(sys.stdin.readline())
print(solution(my_string, k))