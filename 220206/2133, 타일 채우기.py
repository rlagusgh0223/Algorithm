import sys
n = int(sys.stdin.readline())
d = [0] * (n+1)     # 2씩 증가하지만 계산할때와 같은 수의 리스트에 저장하기 위해 n+1개만큼의 리스트를 만든다
                    # 문제에서 0<=n<=30 이라고 했으니까 31을 곱해도 되지만 필요없는 리스트를 만들지 않기 위해 이렇게 만들었다
d[0] = 1

for i in range(2, n+1, 2):  # 2부터 n까지 짝수로 증가한다
    d[i] = d[i-2] * 3
    for j in range(i-4, -1, -2):
        d[i] += 2*d[j]

print(d[n])