# B#, E#은 문제에서 나오지 않았지만
# 34번 테스트케이스가 B#이 나와서 반영하지 않으면 통과하지 못한다
# 나중에 E#이 나올수도 있어 미리 추가했다
# 어차피 없으면 바뀔것도 없으니 결과는 상관없다
def change_melody(melody):
    melody = melody.replace('C#', 'c')
    melody = melody.replace('D#', 'd')
    melody = melody.replace('F#', 'f')
    melody = melody.replace('G#', 'g')
    melody = melody.replace('A#', 'a')
    melody = melody.replace('B#', 'b')
    melody = melody.replace('E#', 'e')
    return melody

def check_time(s, e):
    s = list(map(int, s.split(":")))
    e = list(map(int, e.split(":")))
    return (e[0]*60+e[1]) - (s[0]*60+s[1])

def solution(m, musicinfos):
    answer = '(None)'
    longest_time = -1
    m = change_melody(m)
    for music in musicinfos:
        start_time, end_time, title, melody = music.split(",")

        play_time = check_time(start_time, end_time)
        melody = change_melody(melody)

        melody = (melody*(play_time//len(melody))) + melody[:play_time%len(melody)]
        if m in melody:
            if play_time > longest_time:
                answer = title
                longest_time = play_time
    return answer

import sys

m = sys.stdin.readline().strip()
music = list(sys.stdin.readline().strip().split('", "'))
print(solution(m, music))