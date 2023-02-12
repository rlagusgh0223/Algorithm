from math import factorial
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)] 
print(factorial(2*n)//(factorial(n)**2), n**2)  # 코드 2의 수행 횟수는 주어지는 칸의 횟수와 같다