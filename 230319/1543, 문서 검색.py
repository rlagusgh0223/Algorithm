import sys
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())
cnt = 0
i = 0
while i <= len(a)-len(b):
    if a[i:i+len(b)] == b:
        cnt += 1
        i += len(b)
    else:
        i += 1
print(cnt)



# 내 코드가 좀 더 빠르지만 더 간단해서 위에 올렸다
# 원리는 똑같은것 같다
import sys
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())
cnt = 0
i = 0
while i <= len(a)-len(b):
    ck = True
    for j in range(len(b)):
        if a[i+j] != b[j]:
            ck = False
            break
    if ck:
        i += len(b)
        cnt += 1
    else:
        i += 1
print(cnt)