import sys
n = int(sys.stdin.readline())
lst = []    # 입력되는 값들을 받을 리스트
result = []    # 계산된 결과를 받을 리스트

for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))
    lst[i].sort()    # 입력된 값을 리스트에 넣은 후 오름차순으로 만들어준다
    
    if lst[i][0] == lst[i][1] == lst[i][2]:    # 3개의 값이 같은 경우
        result.append(10000 + lst[i][2]*1000)
    # elif lst[i][0] < lst[i][1] == lst[i][2]:
    elif lst[i][1] == lst[i][2]:    # 오름차순으로 정렬되어 있으므로 2가지 값만 같은 경우
        result.append(1000 + lst[i][1]*100)    # elif문이므로 3개가 값이 같으면 위의 if문에서 걸러진다
    # elif lst[i][0] < lst[i][1] < lst[i][2]:
    elif lst[i][1] < lst[i][2]:    # 하나의 값만 가장 큰 경우
        result.append(lst[i][2] * 100)

print(max(result))