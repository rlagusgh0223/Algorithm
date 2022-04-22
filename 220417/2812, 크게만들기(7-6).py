import sys
N, K = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().rstrip()))
cnt1 = 0    # 출발점

while True:
    if K==0:
        break
    cnt2 = len(number)    # number에서 변수를 빼줘야 하는데 그럼 for문이 바뀌게 되므로 미리 개수를 빼둔다
    for i in range(cnt1, cnt2):
        if number[i] < number[i+1]:    # 왼쪽에 있는 수가 더 크고 아직 다 지우지 않았다면
            del number[i]
            cnt1 -= 1
            K -= 1
            break;
    cnt1 += 1

for i in number:
    print(i,end="")