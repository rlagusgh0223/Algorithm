cord = input().split('-')
check = True
for num in cord:
    now = sum(map(int, num.split('+')))
    if check:
        answer = now
        check = False
    else:
        answer -= now
print(answer)