def solution(array, height):
    # 지금은 숫자가 작으니까 차이가 작지만
    # sort보다 반복문 한번 돌리는게 더 빠르다
    return sum(1 for a in array if a > height)

    # array.sort()
    # for i in range(len(array)):
    #     if array[i] > height:
    #         return len(array) - i
    # return 0

import sys

a = list(map(int, sys.stdin.readline().split(", ")))
h = int(sys.stdin.readline())
print(solution(a, h))