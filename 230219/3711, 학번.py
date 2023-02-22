import sys
N = int(sys.stdin.readline())
for _ in range(N):
    G = int(sys.stdin.readline())
    lst = [int(sys.stdin.readline()) for _ in range(G)]
    m = 0
    while True:
        m += 1
        remain = list(set([now%m for now in lst]))  # set으로 안하고 조건문으로 리스트에 입력 후 비교하면 시간 초과 뜬다
        if len(remain) == len(lst):
            break
    print(m)