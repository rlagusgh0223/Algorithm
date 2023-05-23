# 7개의 수를 더하면 100이므로 총 합에서 두 수를 뺐을때 100이 되는 값을 찾으면 된다
import sys
data = [0] * 9
for i in range(9):
    data[i] = int(sys.stdin.readline())
now = sum(data)
for i in range(8):
    for j in range(i+1, 9):
        if now-data[i]-data[j] == 100:
            # j가 더 뒤의 수 이므로 j를 먼저 지우면 i의 순서는 영향을 받지 않는다
            del data[j]
            del data[i]
            for now in data:
                print(now)
            exit()