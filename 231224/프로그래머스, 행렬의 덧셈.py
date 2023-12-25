def solution(arr1, arr2):
    answer = [[0]*len(arr1[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

import sys
arr1 = list(sys.stdin.readline().strip().split("],["))
arr2 = list(sys.stdin.readline().strip().split("],["))
arr1 = [list(map(int, now.split(","))) for now in arr1]
arr2 = [list(map(int, now.split(","))) for now in arr2]
print(solution(arr1, arr2))