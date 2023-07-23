import sys
while True:
    N = sys.stdin.readline().rstrip()
    if N == '0':
        break
    cnt = len(N) + 1
    for now in N:
        if now == '1':
            cnt += 2
        elif now == '0':
            cnt += 4
        else:
            cnt += 3
    print(cnt)