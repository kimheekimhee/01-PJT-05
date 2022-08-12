import sys

sys.stdin = open("_반반.txt")

t = int(input())

for i in range(1, t+1):
    s = list(input())
    s.sort()
    if s[0] == s[1] and s[2] == s[3] and s[1] != s[2]:
        print(f"#{i} Yes")
    else:
        print(f"#{i} No")



