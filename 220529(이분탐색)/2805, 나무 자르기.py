# 랜선 자르기와 같은 유형이지만 기억하지 못했다
# 모든 나무를 자르는 경우를 생각하지 못했다
import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)

while start <= end:
    mid = (start+end)//2
    num = 0
    for length in tree:
        if length >= mid:
            num += length-mid
    if num >= M:
        start = mid+1
    else:
        end = mid-1

print(end)