# 결국 마지막은 h이고, 나머지는 a이므로
# 문자열의 길이를 비교하면 의사가 원하는 만큼의 소리를 낼 수 있는지 알 수 있다
import sys
A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
if len(A) >= len(B):
    print("go")
else:
    print("no")