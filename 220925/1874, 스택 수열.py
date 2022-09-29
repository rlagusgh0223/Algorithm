import sys
n = int(sys.stdin.readline())
lst = []
stack = []
result = []
num = 0
for i in range(n):
    lst.append(int(sys.stdin.readline()))

for i in range(1, n+1):
    stack.append(i)
    result.append("+")
    while True:
        if len(stack)!=0 and stack[-1] == lst[num]:
            stack.pop()
            result.append("-")
            num += 1
        else:
            break
if stack:
    print("NO")
else:
    for now in result:
        print(now)