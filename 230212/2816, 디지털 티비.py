# 시간이 조금 더 빠르고 메모리는 똑같다.
import sys
N = int(sys.stdin.readline())
n = [sys.stdin.readline().rstrip() for _ in range(N)]
k1, k2 = n.index('KBS1'), n.index('KBS2')
if k1 > k2:  # k1이 k2보다 아래에 있다면 순서를 바꾸면서 k2가 한 칸 아래로 내려온다
    k2 += 1
print('1'*k1 + '4'*k1 + '1'*k2 + '4'*(k2-1))  # KBS2는 두 번째에 있어야 하므로 index에서 1 빼준다(KBS1 자리)



# 예제처럼 결과가 나오지 않아도 KBS1이 첫 번째에, KBS2가 두 번째에만 있으면 된다
# import sys
# N = int(sys.stdin.readline())
# n = [sys.stdin.readline().rstrip() for _ in range(N)]
# i = 0
# ans = []
# while n[i] != 'KBS1':
#     ans.append(1)
#     i += 1
# for j in range(i, 0, -1):
#     ans.append(4)
#     n[j], n[j-1] = n[j-1], n[j]
# i = 0
# while n[i] != 'KBS2':
#     ans.append(1)
#     i += 1
# for j in range(i, 1, -1):
#     ans.append(4)
#     n[j], n[j-1] = n[j-1], n[j]
# print(*ans, sep='')