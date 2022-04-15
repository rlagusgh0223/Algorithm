import sys
K, N, M = map(int, sys.stdin.readline().split())

n = K * N - M    # 부모님께 받아야 하는 돈(개당가격*개수 - 받은돈). 만약 부모님이 주신 돈이 더 많다면 음수가 나온다

if n > 0:    # 부모님이 주신 돈이 더 적으면 받을돈이 되므로 그대로 출력
    print(n)
else:    # 부모님이 주신 돈이 딱 맞거나 더 많으면 받을 돈이 없으므로 0 출력
    print('0')