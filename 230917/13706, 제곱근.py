import sys
N = int(sys.stdin.readline())
start = 0
end = N
while True:
    mid = (start+end) // 2
    if mid * mid == N:
        print(mid)
        break
    elif mid*mid > N:
        end = mid - 1
    else:
        start = mid + 1