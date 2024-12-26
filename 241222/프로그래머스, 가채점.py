def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer

import sys

n = list(map(int, sys.stdin.readline().split(", ")))
o = list(map(int, sys.stdin.readline().split(", ")))
s = list(map(int, sys.stdin.readline().split(", ")))
print(solution(n, o, s))