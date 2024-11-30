def solution(n, info):
    answer = []
    max_diff = 0
    lion = [0] * 11

    def DFS(cnt, idx):
        nonlocal answer, max_diff, lion
        if cnt == n:
            lion_score, appeach_score = 0, 0
            for i in range(11):
                if lion[i] > info[i]:
                    lion_score += 10-i
                elif info[i] > 0:
                    appeach_score += 10-i

            if lion_score > appeach_score:
                diff = lion_score - appeach_score
                if diff > max_diff:
                    max_diff = diff
                    answer = lion[:]
                elif diff == max_diff:
                    for i in range(10, -1, -1):
                        if lion[i] > answer[i]:
                            answer = lion[:]
                            break
                        elif lion[i] < answer[i]:
                            break
            return

        for i in range(idx, 11):
            lion[i] += 1
            DFS(cnt+1, i)
            lion[i] -= 1

    DFS(0, 0)
    return answer if answer else [-1]

import sys

n = int(sys.stdin.readline())
info = list(map(int, sys.stdin.readline().split(",")))
print(solution(n, info))