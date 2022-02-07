import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.reverse()     # 리스트의 배열을 반대로 바꿔주는 함수
d = [1] * n     # 그 자체로도 하나의 길이는 되니까 1로 길이 초기화

for i in range(n):
    for j in range(i+1):
        if A[j] < A[i] and d[j] >= d[i]:    # 리스트 앞의 숫자가 작고 그 숫자까지의 길이가 더 길다면
            d[i] = d[j] + 1                 # 앞 까지의 길이 + 1을 이용해 가장 긴 수열에 현재 리스트 추가한다
    
print(max(d))   # 각 리스트 값 중 가장 큰 값(수열 길이가 가장 긴 값) 출력