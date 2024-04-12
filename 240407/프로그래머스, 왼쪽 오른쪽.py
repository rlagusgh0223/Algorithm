def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            return str_list[:i]
        elif str_list[i] == 'r':
            return str_list[i+1:]
    return []

import sys

str_list = list(sys.stdin.readline().strip().split('", "'))
print(solution(str_list))