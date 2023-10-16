import sys
cnt = 0
while True:
    L, P, V = map(int, sys.stdin.readline().split())
    if L == P == V == 0:
        break
    cnt += 1
    # 총 V일의 휴가 중 연속으로 P일 쉴 수 있는 횟수는 V//P
    # 이 중 L일을 쉴거니까 (V//P)*L
    # 온전히 P일을 쉬지는 못하더라도 쉴 수 있는 날은 V%P
    # V%P일이 L일보다 클 수 있으므로 둘 중 작은 날을 계산한다
    print(f"Case {cnt}: {(V//P)*L + min(V%P, L)}")