# 입력한 리스트 들 중 몇번째로 큰 수인지 출력하는 문제이다
import sys
n = int(sys.stdin.readline())
lst1 = list(map(int, sys.stdin.readline().split()))
lst2 = list(sorted(set(lst1)))  # 몇번째로 큰지 검증하기 위한 수들의 리스트로 동일한 수가 입력된 경우를 없애기 위해 set 이용

# 시간초과 나지 않게 하려면 딕셔너리를 이용해야 한다.
# lst2[i]는 해당 값, i는 lst2에서의 순서이며 딕셔너리를 통해 키와 값으로 입력할 수 있다
dic = {lst2[i]:i for i in range(len(lst2))}

# 딕셔너리에 키값으로 lst1의 값을 입력하면 value값으로 크기 순서가 나온다
for i in lst1:
    print(dic[i], end=' ')



# 이해 안되면 아래 식을 돌려봐라
# for i in range(len(lst2)):
#     print(lst2[i], i)
# print(dic)
# print(dic[-10])
# print(dic[-9])
# print(dic[2])
# print(dic[1])




# 아래 코드 쓰면 시간초과 난다
# cnt = [0] * n

# for i in range(n):    # 확인하려고 하는 현재 위치의 값과
#     for j in lst2:    # 리스트의 다른 값들 중
#         if lst1[i] > j:    # 더 작은 수가 있다면 카운트 증가하여 몇번째로 큰 수인지 입력
#             cnt[i] += 1

# for i in cnt:
#     print(i, end=' ')