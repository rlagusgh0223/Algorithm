def go(W):
    n = len(W)
    if n == 2:
        return 0
    ans = 0
    for i in range(1, n-1):
        energy = W[i-1] * W[i+1]
        b = W[:i] + W[i+1:]
        energy += go(b)
        if ans < energy:
            ans = energy
    return ans

N = int(input())
W = list(map(int, input().split()))
print(go(W))