# 반복문을 이용해서 구하는게 더 쉽지만 이 단원은
# 재귀함수를 공부하는 단원이므로 재귀함수를 이용하겠다
import sys
def fact(N):
    if N>1:
        return N * fact(N-1)
    else:
        return 1
N = int(sys.stdin.readline())
print(fact(N))