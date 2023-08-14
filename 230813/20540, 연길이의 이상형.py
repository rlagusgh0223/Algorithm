import sys
mbti = sys.stdin.readline().rstrip()
MBTI = ['E', 'I' , "S", "N", "T", 'F', "J", 'P']
for now in mbti:
    MBTI.remove(now)
print(*MBTI, sep = '')