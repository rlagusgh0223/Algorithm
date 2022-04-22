import sys
N, K = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().rstrip()))
cnt1 = 0    # 출발점
cnt2 = len(number)    # number에서 변수를 빼줘야 하는데 그럼 for문이 바뀌게 되므로 미리 개수를 빼둔다
k = K    # K개의 개수를 두번 카운트 해야 되서 다른 변수로도 만듦

# 가장 큰 수를 만들기 위해서는 왼쪽에 있는 수가 커야 한다
# for i in range(cnt):
#     if K == 0:
#         break;
#     if number[i] < number[i+1]:    # 왼쪽에 있는 수가 더 크고 아직 다 지우지 않았다면
#         del number[i]
#         i -= 1    # i가 변하지 않아 리스트가 바뀌지 않는다.
#         # cnt에서부터 시작하게 해보자
#         K -= 1
#         print("2:",i)
# print(number)

while True:
    if K==0:
        break
    for i in range(cnt1, cnt2):
        if K == 0:
            break;
        if number[i] < number[i+1]:    # 왼쪽에 있는 수가 더 크고 아직 다 지우지 않았다면
            del number[i]
            cnt1 -= 1
            K -= 1
        cnt1 += 1
    print(cnt1)
print(number)