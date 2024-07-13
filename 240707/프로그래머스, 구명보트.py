def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people) - 1
    while start <= end:
        # 구해야 될 사람들 중 가장 무거운 사람과
        # 가장 가벼운 사람이 동시에 구명보트에 탈 수 있으면
        # 같이 탄걸로 계산한다
        if people[start]+people[end] <= limit:
            start += 1
            end -= 1
        # 가장 가벼운 사람과 같이 가지 못한다면 어차피
        # 같이는 못타므로 그냥 혼자 탄걸로 계산한다
        # 가장 무거운 사람도 혼자서는 보트에 탈 수 있다
        else:
            end -= 1
        # 보트는 최대 2명까지밖에 타지 못하므로 이번에
        # 탈 수 있는 인원은 다 탔다
        answer += 1
    return answer

import sys

people = list(map(int, sys.stdin.readline().split(", ")))
limit = int(sys.stdin.readline())
print(solution(people, limit))