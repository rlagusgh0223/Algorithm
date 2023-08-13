# 뭐가 문제인지 모르겠는데, sys.stdin.readline()으로 하면 출력 형식이 잘못되었다고 오류난다
while True:
    ascii = input()
    if ascii == "***":
        break
    print(ascii[::-1])