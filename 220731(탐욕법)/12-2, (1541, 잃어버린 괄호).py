import sys
num = list(sys.stdin.readline().split('-'))
for i in range(len(num)):
    now = sum(map(int, num[i].split('+')))
    if i == 0:
        answer = now
    else:
        answer -= now
print(answer)