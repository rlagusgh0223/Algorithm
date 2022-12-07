import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
left = right = ans = 0
sum = A[0]
while left <= right and right < N:
    if sum < M:
        right += 1
        if right < N:
            sum += A[right]
    elif sum == M:
        right += 1
        ans += 1
        if right < N:
            sum += A[right]
    elif sum > M:
        sum -= A[left]
        left += 1
        if left > right and left < N:
            sum = A[left]
            right = left
print(ans)