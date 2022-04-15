import sys
while True:    # 0 0 을 입력할 때까지 반복
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:    # 0 0을 입력한다면 종료
        break
    elif n > m:    # 0 0 을 입력하지 않고 앞의 수가 뒤의 수보다 크다면 Yes
        print("Yes")
    else:    # 위의 두 경우를 제외한 모든 경우는 No
        print("No")