import sys
N, M = map(int, sys.stdin.readline().split())
bulb = list(map(int, sys.stdin.readline().split()))
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    b -= 1
    if a == 1:
        bulb[b] = c
    elif a == 2:
        for i in range(b, c):
            bulb[i] = (bulb[i]+1) % 2
    elif a == 3:
        for i in range(b, c):
            bulb[i] = 0
    else:
        for i in range(b, c):
            bulb[i] = 1
print(*bulb)


# 아래 코드는 출력초과 난다.
# 그렇지만 슬라이싱으로 값을 줄 때 어떻게 주는지 기억하려고 남긴다
# import sys
# N, M = map(int, sys.stdin.readline().split())
# bulb = list(map(int, sys.stdin.readline().split()))
# for _ in range(M):
#     a, b, c = map(int, sys.stdin.readline().split())
#     b -= 1
#     if a == 1:
#         bulb[b] = c
#     elif a == 2:
#         bulb[b:c] = [(bulb[i]+1) % 2 for i in range(b, c)]
#     elif a == 3:
#         bulb[b:c] = [0] * (c-b)
#     else:
#         bulb[b:c] = [1] * (c-b)
#     print(*bulb)