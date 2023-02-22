# 다음날 밥 양은 오늘의 양에 4를 곱한것과 같다
# 이걸 어떻게 찾았는지 대단하다
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    p = 1
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    ck = sum(lst)
    while True:
        if ck > N:
            print(p)
            break
        ck *= 4
        p += 1