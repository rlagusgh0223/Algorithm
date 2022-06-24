import sys
n = int(sys.stdin.readline())    # 포도주 잔의 개수 입력
wine = [0 for _ in range(n+1)]    # 포도주 잔의 양을 입력받기 위한 리스트(n개로 해도 계산은 되지만 백준 사이트에서 런타임 에러가 나온다)
for i in range(n):
  wine[i] = int(sys.stdin.readline())

acc = [0]    # 지금까지 누적해서 마신 양을 입력하기 위한 리스트. 반복문에서의 계산을 위해 첫 값은 0으로 한다
acc.append(wine[0])
acc.append(wine[0]+wine[1])    # 세번째 잔 까지 가장 많이 마시는건 첫번째와 두번째 잔을 다 마시는 것이다

for i in range(3, n+1):    # 세번째 잔부터 끝까지 모든 와인에 대해
  acc.append(max(acc[i-1], wine[i-1]+acc[i-2], wine[i-1]+wine[i-2]+acc[i-3]))    # 이번에 마시지 않은 경우, 이번에 마시고 이 앞잔은 마시지 않은 경우, 이번과 이 앞잔은 마시고 2번째 앞잔은 마시지 않은 경우 중 가장 큰 수 입력

print(acc[n])    # 마지막에 입력된 수 출력