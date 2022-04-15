import sys
n = int(sys.stdin.readline())
lst = []

# 1. 입력한 단어들 리스트로 받음
for i in range(n):
    lst.append(sys.stdin.readline().rstrip())

# 2. 중복이 없는 집합 set을 이용하여 중복된 단어 제거
word = list(set(lst))

# 3. 리스트의 단어들 길이와 리스트 단어 묶어서 정렬
for i in range(len(word)):
    word[i] = (len(word[i]), word[i])

# 4. sorted 이용하여 단어 길이 순서대로 리스트 정렬
word = sorted(word)

# 5. 출력해야되는건 단어 뿐이므로 각 리스트의 두번째 값만 출력
for i in word:
    print(i[1])
