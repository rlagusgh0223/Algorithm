# 모범답안
# bin : 10진수를 2진수로 바꿔준다
#       처음 2글자는 0b로 2진수임을 알린다
# (5|3=7, 5&3=1, 5^3=6)
# i|j 비트연산자:or 먼저 적용하고나서 bin:이진변환

# rjust(n, str) : n자리의 문자를 만든다. 자리가 부족하면 일단 가지고 있는 문자를 오른쪽에 두고
# str을 오른쪽에서 왼쪽으로로 채운다
# 반대개념인 ljust는 왼쪽에 문자를 두고 왼쪽부터 오른쪽으로 채워간다
# zfill(n) : n자리수만큼 문자열이 부족하다면 0을 왼쪽에 채워준다

# replace(before, after) : 문자열에서 before 부분을 after로 바꾼다

def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        a12 = bin(a1 and a2)[2:]
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer


import sys
n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split(", ")))
arr2 = list(map(int, sys.stdin.readline().split(", ")))
print(solution(n, arr1, arr2))

def solutions(n, arr1, arr2):
    answer = [['#']*n for _ in range(n)]
    arr1ck, arr2ck = [], []
    for a in arr1:
        now = []
        while a>0:
            now.append(a%2)
            a //= 2
        while len(now) < n:
            now.append(0)
        arr1ck.append(now[::-1])
    for a in arr2:
        now = []
        while a>0:
            now.append(a%2)
            a //= 2
        while len(now) < n:
            now.append(0)
        arr2ck.append(now[::-1])
    for i in range(n):
        for j in range(n):
            if arr1ck[i][j] == arr2ck[i][j] == 0:
                answer[i][j] = ' '
        answer[i] = ''.join(answer[i])
    return answer