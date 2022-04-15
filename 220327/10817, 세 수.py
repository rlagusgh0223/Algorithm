import sys
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()    # 오름차순으로 만들어서 숫자들의 크기 비교한다. 집합이 아니니까 같은 수여도 사라지지 않고 나열된다.
print(lst[-2])    # 두번째로 큰 수니까 뒤에서 두번째 수 출력하게 만든다