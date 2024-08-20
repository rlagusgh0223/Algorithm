def solution(answers):
    check = [0] * 4
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if one[i%5] == answers[i]:
            check[1] += 1
        if two[i%8] == answers[i]:
            check[2] += 1
        if three[i%10] == answers[i]:
            check[3] += 1
    m = max(check)
    return [i for i in range(1, 4) if check[i]==m]

import sys

print(solution(list(map(int, sys.stdin.readline().split(",")))))
