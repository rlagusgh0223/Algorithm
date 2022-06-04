# 선택정렬을 사용하는데, 파이썬의 내장함수는 선택정렬보다 좋다
import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))

for i in range(N):
    for j in range(i+1, N):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for i in lst:
    print(i)