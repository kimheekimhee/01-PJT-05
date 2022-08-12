import sys

sys.stdin = open("_모음이보이지않는사람.txt")
mo = ['a','e','i','o','u']

t = int(input())
for _ in range(1, t+1):
    w = ''
    s = input()
    for i in s:
        if i not in mo:
            w += i
    print(f'#{_} {w}')        
