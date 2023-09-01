# 섬의 모든 마을을 돌아다니는데 최소의 비용을 내려면
# 이동 비용이 가장 비싼 마을에서 출발하면 된다
import sys
n = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split())))
print(sum(lst[:-1]))