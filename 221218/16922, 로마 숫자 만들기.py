lst = [[1, 5, 10, 50]]
N = int(input())
for i in range(1, N):
    num = set()
    for j in range(len(lst[i-1])):
        now = lst[i-1][j]
        num.add(now+1)
        num.add(now+5)
        num.add(now+10)
        num.add(now+50)
    lst.append(list(num))
print(len(lst[-1]))