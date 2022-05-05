# 모범답안
import sys
N = int(sys.stdin.readline())
arr = [int(i) for i in sys.stdin.readline().split()]

s = int(sys.stdin.readline())
while True:    # 리스트에서 왼쪽에 있을 수록 큰 값이 나올때까지 반복
    tof = False    # 종료 지점을 나타내기 위한 변수 선언
    for i in range(N):    # ~16
        idx = i    # i를 기준으로 오른쪽에 있는 수 중 남은 s번 교체해서 바꿀수 있는 최댓값의 위치를 저장할 변수
        cmp = 0    # 교체 횟수를 임시로 저장하는 변수
        for j in range(N-1, i, -1):
            if arr[idx] < arr[j] and j-1 <= s:
                idx = j
                tof = True    # while문이 종료되지 않게 한다
                cmp = j-i
        if idx != i:
            tmp = arr[idx]
            del arr[idx]
            arr.insert(i, tmp)
            s -= cmp
            break
    if tof == False:    # 더 이상 바꿀 수가 없을 때 
        break

print(*arr)

#####################################
# import sys
# N = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))
# S = int(sys.stdin.readline())
# cnt = 0
# for i in range(S):
#     if lst[cnt] < lst[cnt+1]:
#         lst[cnt], lst[cnt+1] = lst[cnt+1], lst[cnt]
#     cnt += 2

# for i in range(N-1):
#     print(lst[i],end=' ')
# print(lst[-1])