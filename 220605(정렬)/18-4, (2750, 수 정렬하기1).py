# 선택정렬
# sort()쓰는게 훨씬 빠르지만 코드를 기억하기 위해 아래 선택정렬 사용
import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))

for i in range(N):
    for j in range(i+1, N):
        if lst[i] > lst[j]:
            lst[j], lst[i] = lst[i], lst[j]
    
for i in lst:
    print(i)