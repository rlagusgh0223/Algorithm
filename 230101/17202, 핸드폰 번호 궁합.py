import sys
input = sys.stdin.readline
A = list(map(int, list(input().rstrip())))
B = list(map(int, list(input().rstrip())))
ans = [0] * (len(A)*2)
for i in range(0, len(A)*2-1, 2):
    ans[i] = A[i//2]
    ans[i+1] = B[i//2]
while len(ans) > 2:
    for i in range(len(ans)-1):
        ans[i] = (ans[i]+ans[i+1])%10
    ans.pop()
print(''.join(map(str, ans)))