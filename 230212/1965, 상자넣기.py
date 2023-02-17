import sys
n = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
lst = [1] * n  # 아무것도 넣을 수 없을경우 해당 박스만 따져서 1로 준다
for i in range(1, n):  # 지금 박스를
    for j in range(i):  # 이 앞까지의 박스와 비교
        if box[i] > box[j]:
            lst[i] = max(lst[i], lst[j]+1)
print(max(lst))