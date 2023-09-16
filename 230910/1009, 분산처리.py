# 아래 코드는 시간초과
# import sys
# T = int(sys.stdin.readline())
# for _ in range(T):
#     a, b = map(int, sys.stdin.readline().split())
#     now = (a**b) % 10
#     if now == 0:
#         print(10)
#     else:
#         print(now)


# 1부터 10까지 각각을 거듭제곱 했을 때 일의자리 패턴
# 1     1
# 2     2, 4, 6, 8
# 3     3, 9, 7, 1
# 4     4, 6
# 5     5
# 6     6
# 7     7, 9, 3, 1
# 8     8, 4, 2, 6
# 9     9, 1
# 10    0

# 패턴 1: 1, 5, 6, 10
# 패턴 2: 4, 9
# 패턴 3: 2, 3, 7, 8

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    aa = a%10
    if aa == 0:  # 패턴 1의 10
        print(10)
    elif aa in [1, 5, 6]:  # 패턴 1
        print(aa)
    elif aa in [4, 9]:  # 패턴 2
        bb = b % 2
        if bb == 0:
            print((aa*aa) % 10)
        else:
            print(aa)
    else:  # 패턴 4
        bb = b % 4
        if bb == 0:
            print((aa**4) % 10)
        else:
            print((aa**bb) % 10)