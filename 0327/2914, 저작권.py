import sys
A, I = map(int, sys.stdin.readline().split())
print(A * (I-1) + 1)    # 평균값 I가 소수점이면 올림을 이용해 정수로 만든 값이니까 1을 빼는건 알겠는데, 나중에 왜 1을 더하는지는 모르겠다.