import sys

sys.stdin = open("_반반.txt")


for _ in range(int(input())):
    s = sorted(list(input()))
    print("#{} {}".format(_+1, 'Yes' if s[0]==s[1] and s[2]==s[3] and s[1] != s[2] else 'No'))