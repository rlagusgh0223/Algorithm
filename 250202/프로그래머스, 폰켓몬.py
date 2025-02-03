def solution(nums):
    return min(len(nums)//2, len(set(nums)))


import sys

print(solution(list(map(int, sys.stdin.readline().split(",")))))