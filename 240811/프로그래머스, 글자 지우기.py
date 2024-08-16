def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:
            answer += my_string[i]
    return answer

import sys

my_string = sys.stdin.readline().strip()
indices = list(map(int, sys.stdin.readline().split(", ")))
print(solution(my_string, indices))