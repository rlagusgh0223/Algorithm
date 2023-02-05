import sys
N = int(sys.stdin.readline())
lst = bin(N)[2:][::-1]  # bin() : 10진수를 0b2진수로 표현해주는 함수. 그래서 앞의 2자리를 떼고 문자열을 뒤집어줌
lst = int(lst, 2)  # 뒤집힌 2진수를 다시 10진수로 변환
print(lst)


# import sys
# N = int(sys.stdin.readline())
# lst = []
# ans = 0
# while N != 0:
#     lst.append(N%2)
#     N //= 2
# for i in range(len(lst)):
#     ans += (2**i) * lst[len(lst)-1-i]
# print(ans)