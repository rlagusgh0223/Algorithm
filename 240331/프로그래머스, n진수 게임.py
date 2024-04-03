def calculate(number, n):
    # 16진법까지 가능한 모든 수를 적는다
    ck = "0123456789ABCDEF"
    result = ''
    while number > 0:
        # divmod: 괄호 안의 수를 나눠서
        # 몫과([0]/[1]) 나머지를([0]%[1]) 한번에 구한다
        number, mod = divmod(number, n)
        # 입력받은 수의 나머지는 n진법의 수이므로
        # ck에서 해당하는 수를 result에 문자열로 더한다
        result += ck[mod]
    return result[::-1]

def solution(n, t, m, p):
    # n진법 계산할때 0보다 큰 경우를 계산할건데
    # 0이 입력되면 계산이 되지 않는다
    # 어차피 모든 진법에서 0은 0이므로 그냥 처음에 0을 넣고
    # 1부터 시작하게 한다
    answer = '0'
    
    # 사람 수 만큼 각자 말할 숫자를 말하고
    # 그 수를 모두 입력한다
    for number in range(1, t*m):
        answer += calculate(number, n)
    
    # 튜브(사용자)가 말하는 수들을 내야 되므로
    # 처음 튜브는 p-1이다(순서는 1부터 계산하므로 리스트에서는 1을 빼야된다)
    # 이후 m씩 더해 튜브의 순서를 파악한다
    return answer[p-1:t*m:m]

import sys

n, t, m , p = map(int, sys.stdin.readline().split())
print(solution(n, t, m, p))