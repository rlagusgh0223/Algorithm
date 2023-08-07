# 파이썬은 어차피 시간 오래걸리고 sort이용하는것보다 min(), max()이용하는게 그나마 더 빠르다
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(min(lst), max(lst))