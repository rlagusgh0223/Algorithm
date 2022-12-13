def change(num, index, digit):
    if index==0 and digit==0:
        return -1
    s = list(str(num))
    s[index] = chr(digit+ord('0'))
    return int(''.join(s))

from collections import deque
prime = [False] * 10001
for i in range(2, 10001):
    if prime[i] == False:
        for j in range(i*i, 10001, i):
            prime[j] = True
for i in range(10001):
    prime[i] = not prime[i]
t= int(input())
for _ in range(t):
    n, m = map(int, input().split())
    c = [False] * 10001
    c[n] = True
    d = [0] * 10001
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        for i in range(4):
            for j in range(10):
                nxt = change(now, i, j)
                if nxt!=-1 and prime[nxt] and c[nxt]==False:
                    c[nxt] = True
                    d[nxt] = d[now] + 1
                    q.append(nxt)
    print(d[m])