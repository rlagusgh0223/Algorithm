def solution(my_string, s, e):
    # my_string[e:s-1:-1]로 할 경우 s가 0이면 -1이 되어 에러가 된다
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

import sys

my_string = sys.stdin.readline().strip()
s, e = map(int, sys.stdin.readline().split())
print(solution(my_string, s, e))