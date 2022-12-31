N = int(input())
cnt = 0
while N > 10:
    N //= 10
    cnt += 1
cnt += 1
print(cnt)

# N = input()
# S = '1' * len(N)
# if len(N) == 1:
#     print(1)
# elif int(N) >= int(S):
#     print(len(N))
# else:
#     print(len(N)-1)