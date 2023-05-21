# A : 택희, B : 영훈, C : 남규
import sys
N = int(sys.stdin.readline())
ans = 0
for A in range(2, N-2, 2):  # 택희는 짝수개로 받으며, 영훈과 남규가 받기 위해 최소 3개는 남겨둬야 한다
    for B in range(1, N-4):  # 최소한 택희 2개, 영훈이는 3개를 가져야 하므로 남겨두고 계산한다
        for C in range(B+2, N-2):  # 최소한 택희 2개, 남규 1개 받을 사탕은 남겨둔다
            if A+B+C == N:
                ans += 1
print(ans)