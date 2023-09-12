# except에 print넣으면 print안의 내용 출력 안된다
# 입력받을땐 input()으로 하거나 sys.stdin.readline().rstrip()으로 해야된다
import sys
cnt = 0
while sys.stdin.readline().rstrip():
    try:
        cnt += 1
    except:
        break
print(cnt)