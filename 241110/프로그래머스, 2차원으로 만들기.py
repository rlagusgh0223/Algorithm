def solution(num_list, n):
    answer = []
    for x in range(0, len(num_list), n):
        answer.append(num_list[x:x+n])
    return answer

import sys

num = list(map(int, sys.stdin.readline().split(", ")))
n = int(sys.stdin.readline())
print(solution(num, n))