# 가장 큰 약수를 구하는 함수
def get_max(n):
    if n == 1:
        return 0
    data = [1]  # 약수를 저장할 리스트
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            data.append(i)
            # 약수는 짝이 있다
            # ex) 10의 약수로 (1, 10), (2, 5)...
            # 가장 작은 약수를 구했으면 그 약수의 상대는 가장 큰 약수이다
            # 그 중에서 조건에 만족하는 약수를 구한다
            # 도로에 깔린 숫자는 1부터 10^7까지만 있다
            if n//i <= 10000000:
                return n//i
    # n**0.5까지 n//i의 값이 10^7보다 크다면
    # 현재 입력한 약수 중에 가장 큰 값을 리턴한다
    # data에는 i를 입력했으므로 이게 가장 큰 약수다
    return data[-1]

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        answer.append(get_max(i))
    return answer



import sys

b, e = map(int, sys.stdin.readline().split())
print(solution(b, e))