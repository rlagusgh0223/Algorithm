import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
arr = []

for i in range(M, N+1):    # M 이상 N 이하의 수
    if i == 1:    # 만약 1이면 소수가 아니므로 넘어간다
        continue
    elif i == 2:    # 1은 소수가 아니라 2부터 계산해야 되는데 아래 식으로는 2를 계산할 수 없다. 어차피 2는 소수니까 그냥 입력
        arr.append(i)
    else:
        for j in range(2, i):    # 현재 수에 나눌 수 2부터 자기자신까지 반복
            if i%j == 0:    # 자기 자신 전에 나누어 떨어지면 소수가 아니므로 종료
                break
            elif j == i-1:    # 나누어 떨어지는게 자기 자신이면 소수
                arr.append(i)

if not arr:
    print('-1')
else:
    print(sum(arr))
    print(min(arr))