# 아직 잘 모르겠다. 좀 더 연구 필요

import sys

def stars(n):
    arr = []    # 일차원 리스트 형태로 별의 모양을 받을 리스트
    for i in range(3 * len(n)):    # 여기서 n은 별 모양 리스트니까 len으로 바꿔서 만들어준다
        if i // len(n) == 1:    # 가운데 들어가는 부분은 공백
            arr.append(n[i%len(n)] + " "*len(n) + n[i % len(n)])
        else:
            arr.append(n[i % len(n)] * 3)
    return arr

star = ["***", "* *", "***"]   # 가장 작은 형태 기본 모양
n = int(sys.stdin.readline())
k = 0
while n != 3:    # 가장 작은 형태 기본 모양을 기준으로 몇 번 가운데 공백 문양을 만들어야 하는지 계산
    n = n//3    # ex. 27을 입력하면 기본 모양을 기준으로 2번 더 가운데 빈 공간을 만드는 재귀함수 사용
    k += 1

for i in range(k):    # 위에서 만든 별 리스트를 star에 넘겨주고 출력
    star = stars(star)
for i in star:    # 일차원 리스트로 받은 별 모양을 값 별로 출력하여 문제에서 나온 모양대로 만듬
    print(i)







# import sys

# def star(n):
#     global Map
#     if n == 3:   # 기본 모양에 맞춰서 1과 0 입력
#         Map[0][:3] = Map[2][:3] = [1]*3
#         Map[1][:3] = [1, 0, 1]

#     a = n//3
#     star(a)
#     for i in range(3):
#         for j in range(3):
#             if i == 1 and j == 1:    # 사각형 모양의 중간일때(0, 1, 2) 중 1은 중간
#                 continue    # 그냥 지나가게 함으로써 공백을 남긴다
#             for k in range(a):
#                 Map[a*i+k][a^j:a*(j+1)] = Map[k][:a]                

# n = int(sys.stdin.readline())
# Map = [[0 for i in range(n)] for i in range(n)]
# star(n)

# for i in Map:    # Map 리스트에 맞춰서 * 출력
#     for j in i:
#         if j:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()