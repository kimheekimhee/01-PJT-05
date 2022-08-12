import sys

sys.stdin = open("_반반.txt")

tc = int(input())
s = []

for i in range(1, tc + 1):
    c = ord(input())
    s.append(list(c))
    o = sorted(s)
    
print(o)
