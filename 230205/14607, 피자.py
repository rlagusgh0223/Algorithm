# 10^9이므로 dp를 쓰면 시간 초과가 된다
import sys
N = int(sys.stdin.readline())
print((N*(N-1))//2)