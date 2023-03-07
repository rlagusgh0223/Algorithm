import sys
N = int(sys.stdin.readline())
lst = []
for i in range(1, N+1):
    lst += list(str(i))  # 무슨차이인지는 모르겠는데 리스트를 int로 바꾸고 count하면 58점이 나온다
print(lst.count('3') + lst.count('6') + lst.count('9'))