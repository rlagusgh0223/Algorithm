# 사실 sorted를 써버려서 정렬을 만드는 것에 의미는 없는거 같지만
# 문제에서 요구한건 몇번째에 교환되는 수 들을 출력하는거 였으므로 그냥 사용했다.
# sorted를 사용하지 않고 A.index(max(A[:i+1]))를 이용해서 구하면 시간이 훨씬 더 걸린다
import sys
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
a = sorted(A)
cnt = 0
for i in range(N-1, -1, -1):
    ai = a.pop()
    if ai != A[i]:
        cnt += 1
        if cnt == K:
            print(A[i], A[A.index(ai)])
            exit()
        A[A.index(ai)], A[i] = A[i], A[A.index(ai)]
print(-1)