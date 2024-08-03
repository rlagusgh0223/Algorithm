def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        s, e = parts[i]
        answer += my_strings[i][s:e+1]
    return answer

import sys

my_strings = list(sys.stdin.readline().strip().split('", "'))
parts = list(sys.stdin.readline().strip().split("], ["))
parts = [list(map(int, p.split(", "))) for p in parts]
print(solution(my_strings, parts))