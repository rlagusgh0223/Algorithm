import sys
T = int(sys.stdin.readline())
for _ in range(T):
    # 100센트가 1달러인데이고, 동전들 단위는 센트인데
    # 입력할때 센트로 줬으므로 동전의 계산도 달러 기준이 아닌 센트로 바꿔서 계산한다
    C = int(sys.stdin.readline())
    Q = C // 25
    C %= 25
    D = C // 10
    C %= 10
    N = C // 5
    P = C % 5
    print(Q, D, N, P)