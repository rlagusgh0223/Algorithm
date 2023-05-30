import sys
while True:
    word = sys.stdin.readline().rstrip()
    cnt = 0
    if word == '#':
        break
    cnt += word.count('A')
    cnt += word.count('a')
    cnt += word.count('E')
    cnt += word.count('e')
    cnt += word.count('I')
    cnt += word.count('i')
    cnt += word.count('O')
    cnt += word.count('o')
    cnt += word.count('U')
    cnt += word.count('u')
    print(cnt)


# 위의 풀이와 시간과 메모리는 똑같다
import sys
while True:
    word = sys.stdin.readline().rstrip()
    cnt = 0
    if word == '#':
        break
    for now in word:
        if now=='A' or now=='a':
            cnt += 1
        elif now=='E' or now=='e':
            cnt += 1
        elif now=='I' or now=='i':
            cnt += 1
        elif now=='O' or now=='o':
            cnt += 1
        elif now=='U' or now=='u':
            cnt += 1
    print(cnt)