def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer

import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
print(solution(str1, str2))