def solution(price, money, count):
    answer = 0
    for n in range(1, count+1):
        money -= price*n
    if money < 0:
        answer = money * -1
    return answer

import sys
price, money, count = map(int, sys.stdin.readline().split())
print(solution(price, money, count))