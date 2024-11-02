def solution(answers):
    answer = [0] * 3
    check = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == check[j][i%len(check[j])]:
                answer[j] += 1
    m = max(answer)
    return [i+1 for i in range(3) if answer[i]==m]

import sys

a = list(map(int, sys.stdin.readline().split(",")))
print(solution(a))