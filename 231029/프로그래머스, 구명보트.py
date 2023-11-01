# 2명밖에 태울 수 없으므로 우선 가장 무거운 사람과 가벼운 사람이 탈 수 있는지 본다
# 한꺼번에 탈 수 있으면 태우고 안되면 가장 무거운 사람만 태운다
# 한명밖에 안 남아서 start와 end가 같아진다고 해도 어차피 1번은 더 태워야 되므로 answer+=1은 해야되고,
# 이후 start와 end가 어떻게 되든 반복문은 나오게 된다
def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
    return answer

import sys
people = list(map(int, sys.stdin.readline().split()))
limit = int(sys.stdin.readline())
print(solution(people, limit))