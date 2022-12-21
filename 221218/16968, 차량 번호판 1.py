num = list(input())
if num[0] == 'c':
    ans = 26
elif num[0] == 'd':
    ans = 10
for i in range(1, len(num)):
    if num[i] == 'c':
        if num[i] == num[i-1]:
            ans *= 25
        else:
            ans *= 26
    elif num[i] == 'd':
        if num[i] == num[i-1]:
            ans *= 9
        else:
            ans *= 10
print(ans)