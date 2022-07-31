cord = list(input().split('-'))

for i in range(len(cord)):
    now = sum(map(int, cord[i].split('+')))
    if i==0:
        answer = now
    else:
        answer -= now

print(answer)