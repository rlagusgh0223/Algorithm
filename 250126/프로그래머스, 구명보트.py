def solution(people, limit):
    answer, start, end = 0, 0, len(people)-1
    people.sort()
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        # 보트에는 2명만 탈 수 있는데
        # 제일 가벼운 사람이랑 무거운 사람이 같이 갈 수 있다면 같이 가면 되고
        # 제일 가벼운 사람이랑 탈 수 없다면 가장 무거운 사람 혼자 타야된다
        end -= 1
        answer += 1
    return answer

import sys

p = list(map(int, sys.stdin.readline().split(", ")))
l = int(sys.stdin.readline())
print(solution(p, l))