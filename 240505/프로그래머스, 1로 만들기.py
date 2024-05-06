def solution(num_list):
    answer = 0
    for n in num_list:
        while n != 1:
            if n%2 == 1:
                n -= 1
            n /= 2
            answer += 1
    return answer

import sys

num_list = list(map(int, sys.stdin.readline().split(", ")))
print(solution(num_list))