def solution(start_num, end_num):
    answer = [n for n in range(start_num, end_num+1)]
    return answer

import sys

start_num, end_num = map(int, sys.stdin.readline().split())
print(solution(start_num, end_num))
