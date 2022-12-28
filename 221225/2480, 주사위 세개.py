lst = sorted(list(map(int, input().split())))
if len(set(lst)) == 1:
    print(10000 + lst[0]*1000)
elif len(set(lst)) == 2:
    print(1000 + lst[1]*100)  # lst[1]은 lst[0]이나 lst[2]와 같은 값이다
else:
    print(lst[2]*100)