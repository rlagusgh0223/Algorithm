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



# import sys
# T = int(sys.stdin.readline())
# for _ in range(T):
#     p = 1
#     N = int(sys.stdin.readline())
#     lst = list(map(int, sys.stdin.readline().split()))
#     ck = [0] * 6
#     while True:
#         if sum(lst) > N:
#             print(p)
#             break
#         ck[0] = lst[5] + lst[1] + lst[3]
#         ck[5] = lst[4] + lst[0] + lst[2]
#         for i in range(1, 5):
#             ck[i] = lst[i-1] + lst[i+1] + lst[(i+3)%6]
#         lst = [lst[i]+ck[i] for i in range(6)]
#         p += 1