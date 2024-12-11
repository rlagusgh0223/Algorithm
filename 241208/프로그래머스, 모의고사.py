def solution(answers):
    check = [0]*3
    math = [[1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == math[j][i%len(math[j])]:
                check[j] += 1
    ck = max(check)
    return [i+1 for i in range(len(check)) if ck == check[i]]

import sys

a = list(map(int, sys.stdin.readline().split(",")))
print(solution(a))