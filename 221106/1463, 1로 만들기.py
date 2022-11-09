# 파이썬은 다이나믹 프로그래밍은 바텀 업 방식으로 푸는게 좋다
# 재귀를 사용하면 시간이 너무 오래 걸리고 메모리도 많이 차지하기 때문
import sys
N = int(sys.stdin.readline())
lst = [0] * (N+1)
for i in range(2, N+1):
    lst[i] = lst[i-1] + 1
    if i%2==0 and lst[i] > lst[i//2]+1:
        lst[i] = lst[i//2] + 1
    if i%3==0 and lst[i] > lst[i//3]+1:
        lst[i] = lst[i//3] + 1
print(lst[-1])