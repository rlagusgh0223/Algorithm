import sys
T = [0] * 10
T[0] = int(sys.stdin.readline())
ck = abs(T[0]-100)
ans = T[0]
for i in range(1, 10):
    T[i] = T[i-1] + int(sys.stdin.readline())
    if ck >= abs(T[i]-100):
        ck = abs(T[i]-100)
        ans = T[i]
print(ans)