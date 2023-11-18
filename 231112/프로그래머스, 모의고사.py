def solution(answers):
    answer = []
    ans = [0]*4
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for a in range(len(answers)):
        if answers[a] == one[a%len(one)]:
            ans[1] += 1
        if answers[a] == two[a%len(two)]:
            ans[2] += 1
        if answers[a] == three[a%len(three)]:
            ans[3] += 1
    for a in range(len(ans)):
        if ans[a] == max(ans):
            answer.append(a)
    return answer

import sys
answer = list(map(int, sys.stdin.readline().strip().split(",")))
print(solution(answer))