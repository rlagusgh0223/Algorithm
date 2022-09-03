M, N = map(int, input().split())

def search(now):
    if now == 1:
        return False
    else:
        for i in range(2, int(now**0.5)+1):
            if now%i == 0:
                return False
    return True

for i in range(M, N+1):
    if search(i):
        print(i)