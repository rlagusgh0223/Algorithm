import sys
a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

b += c    # 분 단위로 입력된 수 끼리 더한다

if (b // 60) >= 1:    # c는 1000까지 가능하므로 분을 더한게 60분이 넘으면 동작
    a += b//60    # 우선 분에서 차감되는 수를 감안하여 시간에 더해준다
    b -= (b//60) * 60    # 60분 이상 되는 수는 빼준다
if (a // 24) >= 1:    # 시간과 분을 더한 결과가 24시 이상 되면 동작
    a -= (a//24) * 24    # 24시 이상 되는 수는 빼준다

print(a, b)