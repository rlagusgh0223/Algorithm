# 함수로 만들어두면 break를 여러번 할 필요가 없다
# 시간도 훨씬 빠르다
def TEST(K):
    for i in ans:
        for j in ans:
            for k in ans:
                if i+j+k == K:
                    print(i, j, k)
                    return
    print(0)

import sys
lst = [0] * 1001
ans = []
for i in range(2, 1001):
    if lst[i] == 0:
        ans.append(i)
        j = 1
        while i*j <= 1000:
            lst[i*j] = 1
            j += 1
T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    TEST(K)