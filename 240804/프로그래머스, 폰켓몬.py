# 가져갈 수 있는 폰켓몬의 종류는
# N/2마리의 폰켓몬, 폰켓몬의 종류 중 더 작은값이다
# 종류가 N/2보다 많아도  N/2마리만 가져갈 수 있으므로 N/2의 종류만 가져갈 수 있고
# 종류가 N/2보다 적다면 종류 만큼의 폰켓몬 종류만 가져갈 수 있기 때문이다
def solution(nums):
    return min(len(nums)//2, len(set(nums)))

import sys

print(solution(list(map(int, sys.stdin.readline().split(",")))))
