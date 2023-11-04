def solution(want, number, discount):
    answer = 0
    for start in range(len(discount)-9):
        num = [x for x in number]
        for i in range(start, start+10):
            today = discount[i]
            if today in want:
                if num[want.index(today)] > 0:
                    num[want.index(today)] -= 1
        if sum(num) == 0:
            answer += 1
    return answer

import sys
want = list(sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
discount = list(sys.stdin.readline().split())
print(solution(want, number, discount))