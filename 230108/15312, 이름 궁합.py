import sys
A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())
ck = []
alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
for i in range(len(A)):
    ck.append(A[i])
    ck.append(B[i])
for i in range(len(ck)):
    ck[i] = alpha[ord(ck[i])-65]
while len(ck) > 2:
    for i in range(len(ck)-1):
        ck[i] = (ck[i]+ck[i+1])%10
    ck.pop()
print(''.join(map(str, ck)))