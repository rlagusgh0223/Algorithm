import sys
N = int(sys.stdin.readline())
for _ in range(N):
    lst = list(sys.stdin.readline().rstrip())
    lst[0] = lst[0].upper()  # .upper()만 쓰면 원본은 바뀌지 않는다
    print(*lst, sep='')