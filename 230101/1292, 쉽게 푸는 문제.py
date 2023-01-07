import sys
A, B = map(int, sys.stdin.readline().split())
cnt = 1  # 리스트에 입력할 수
lst = []
while cnt <= B:
    for i in range(cnt):
        lst.append(cnt)
    cnt += 1
print(sum(lst[A-1:B]))