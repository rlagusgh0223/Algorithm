import sys
N = int(sys.stdin.readline())
ans = 0
start = length = 1
while start <= N:
    end = start*10 - 1
    if end > N:
        end = N
    ans += (end-start+1) * length
    start *= 10
    length += 1
print(ans)