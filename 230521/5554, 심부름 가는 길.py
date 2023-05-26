import sys
# 반복문을 이용해서 아예 처음부터 ans에 값을 더하는 방법도 있다
# 그렇게 되면 메모리를 더 아낄 수 있다
lst = [int(sys.stdin.readline()) for _ in range(4)]
ans = sum(lst)
print(ans//60)
print(ans%60)