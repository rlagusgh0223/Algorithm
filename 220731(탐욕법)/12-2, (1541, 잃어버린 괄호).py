import sys
cord = sys.stdin.readline().split('-')
answer = 0
for num in cord:
    print(type(num))
    now = sum(map(int, num.split('+')))
    if answer == 0:
        answer = now
    else:
        answer -= now
print(answer)

for i in range(len(cord)):
    print(type(cord[i]))
    now = sum(map(int, cord[i].split('+')))
    if i == 0:
        answer = now
    else:
        answer -= now

print(answer)