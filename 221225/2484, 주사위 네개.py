def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:
        return 50000 + lst[0]*5000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]:  # 같은눈이 3개, 1개로 나뉜 경우
            return 10000 + lst[1]*1000
        else:  # 같은눈이 2개, 2개 나온 경우
            return 2000 + (lst[1]+lst[2])*500
    for i in range(3):
        if lst[i] == lst[i+1]:
            return 1000 + lst[i]*100
    return max(lst) * 100

N = int(input())
print(max(money() for _ in range(N)))