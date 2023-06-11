import sys
n = int(sys.stdin.readline())
start = 0
end = n
while start <= end:
    mid = (start+end) // 2
    if mid**2 < n:
        start = mid + 1
    else:
        end = mid - 1  # 제곱이 n 이상인 것 중에 가장 작은 값을 찾아야 하므로 mid**2가 n과 같더라도 일단 mid값을 줄인다
print(start)