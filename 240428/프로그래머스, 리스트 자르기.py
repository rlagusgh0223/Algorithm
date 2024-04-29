def solution(n, slicer, num_list):
    answer = []
    a, b, c = slicer[0], slicer[1], slicer[2]
    if n == 1:
        answer = num_list[:b+1]
    elif n == 2:
        answer = num_list[a:]
    elif n == 3:
        answer = num_list[a:b+1]
    elif n == 4:
        answer = num_list[a:b+1:c]
    return answer

import sys

n = int(sys.stdin.readline())
slicer = list(map(int, sys.stdin.readline().split(", ")))
num_list = list(map(int, sys.stdin.readline().split(", ")))
print(solution(n, slicer, num_list))