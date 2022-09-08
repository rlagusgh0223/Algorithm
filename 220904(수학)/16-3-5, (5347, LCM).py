from re import L


def LCM(a, b):
    return (a*b) // GCD(a, b)

def GCD(a, b):
    if b%a:
        return GCD(b%a, a)
    else:
        return a

n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append(LCM(a, b))

for now in arr:
    print(now)