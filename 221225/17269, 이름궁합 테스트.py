num = [3,2,1,2,4, 3,1,3,1,1, 3,1,3,2,1, 2,2,2,1,2, 1,1,1,2,2,1]
N, M = map(int, input().split())
A, B = input().split()
lst = []
min_len = min(N, M)
for i in range(min_len):
    lst += A[i] + B[i]
lst += A[min_len:] + B[min_len:]
lst = [num[ord(now)-ord('A')] for now in lst]

for i in range(N+M-2):
    for j in range(N+M-i-1):
        lst[j] += lst[j+1]

print("{}%".format(lst[0]%10*10+lst[1]%10))