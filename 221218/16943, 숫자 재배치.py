def go(index, num):
    if index == n:
        return num
    ans = -1
    for i in range(n):
        if check[i]:
            continue
        if index==0 and A[i]==0:
            continue
        check[i] = True
        temp = go(index+1, num*10 + A[i])
        if temp < B:
            if ans==-1 or ans<temp:
                ans = temp
        check[i] = False
    return ans

A, B = input().split()
A = list(map(int, A))
n = len(A)
B = int(B)
check = [False] * n
print(go(0, 0))