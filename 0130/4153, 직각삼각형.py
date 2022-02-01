import sys
while True:
    x = list(map(int, sys.stdin.readline().split()))
    max_num = max(x)
    if x[0]==0 and x[1]==0 and x[2]==0:
        break
    
    # del은 인덱스로 삭제하고 remove는 값으로 삭제한다
    # del x[0]
    # x.remove(2)
    x.remove(max_num)
    if max_num == (x[0]**2 + x[1]**2)**(1/2):
        print('right')
    else:
        print('wrong')