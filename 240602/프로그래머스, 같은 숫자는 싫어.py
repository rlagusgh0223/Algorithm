def solution(arr):
    answer = []
    for a in arr:
        # answer[-1]!=a를 하면 answer가 비었을 경우에는 에러가 나오지만
        # 둘 다 리스트인 answer[-1:]!=[a]를 하면 리스트가 비었더라도 
        # 리스트 자체를 비교하는 것이므로 에러가 나오지 않는다
        if answer[-1:]!=[a]:
            answer.append(a)
    return answer

import sys

arr = list(map(int, sys.stdin.readline().split(",")))
print(solution(arr))