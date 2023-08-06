import sys
while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    while True:
        n = sum(list(map(int, str(n))))
        if n // 10 == 0:
            print(n)
            break