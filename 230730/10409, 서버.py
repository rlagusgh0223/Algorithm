import sys
n, T = map(int, sys.stdin.readline().split())
time = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    if sum(time[:i+1]) > T:
        print(i)
        exit()
print(n)  # 반복문이 종료될 때까지 일하는 시간이 T보다 작은 경우 n을 출력한다

# 빠르기는 이게 더 빠르다
# import sys
# n, T = map(int, sys.stdin.readline().split())
# time = list(map(int, sys.stdin.readline().split()))
# cnt = 0
# work = 0
# for now in time:
#     if work + now <= T:
#         work += now
#         cnt += 1
#     else:
#         break
# print(cnt)