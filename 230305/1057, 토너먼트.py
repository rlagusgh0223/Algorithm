import sys
N, x, y = map(int, sys.stdin.readline().split())
cnt = 0
while x != y:
    # 원래는 그냥 x - x//2, y- y//2하면 되지만
    # 이해를 쉽게하기 위해 아래처럼 코딩했다.
    # 토너먼트가 계속될 수록 사람은 반으로 줄어드니까
    # 서로가 같아질때까지 2로 나눠준다
    # 이때 홀수로 입력된 수는 1을 더해줘야지 안그러면 앞의 짝수랑 합쳐져 버린다
    if x%2==0:
        x //= 2
    else:
        x = x//2+1
    if y%2==0:
        y //= 2
    else:
        y = y//2+1
    cnt += 1
print(cnt)