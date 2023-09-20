import sys
N, A, B = map(int, sys.stdin.readline().split())
# 문제에서 N <= B라고 했으므로 N이 B보다 큰 경우는 계산할 필요 없다
if A < B:
    print("Bus")
elif A > B:
    print("Subway")
else:
    print("Anything")