import sys
mobis = list("MOBIS")
for now in sys.stdin.readline().rstrip():
    if now in mobis:
        del mobis[mobis.index(now)]
print("YES" if len(mobis)==0 else "NO")