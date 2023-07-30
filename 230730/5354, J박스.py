import sys
T = int(sys.stdin.readline())
for _ in range(T):
    J = int(sys.stdin.readline())
    for i in range(J):
        if i == 0 or i == J-1:
            print("#" * J)
        else:
            print("#"+"J" * (J-2)+"#")
    print()  # 이거 안 하면 출력형식 틀렸다고 한다. 예제 결과를 잘 보자