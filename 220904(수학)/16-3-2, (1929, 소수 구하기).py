M, N = map(int, input().split())

def decimal(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

for i in range(M, N+1):
    if decimal(i):
        print(i)