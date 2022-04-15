import sys
N = int(sys.stdin.readline())

cnt0 = 0
cnt1 = 0

# 입력받은 값 중 안예쁜지(0), 예쁜지(1) 숫자 카운트
for i in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        cnt0 += 1
    else:
        cnt1 += 1

# 안예쁘다는 의견이 많을 경우, 예쁘다는 의견이 많을 경우 출력
# 사람의 수는 홀수이므로 카운트 수가 같을일은 없다.
if cnt0 > cnt1:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")