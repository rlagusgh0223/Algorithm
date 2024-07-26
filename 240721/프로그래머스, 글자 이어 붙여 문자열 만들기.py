def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer


import sys

my_string = sys.stdin.readline().strip()
index_list = list(map(int, sys.stdin.readline().split(", ")))
print(solution(my_string, index_list))