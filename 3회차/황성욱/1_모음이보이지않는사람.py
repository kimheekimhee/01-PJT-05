import sys

sys.stdin = open("_모음이보이지않는사람.txt")
t = int(input())
for i in range(t):
    s = input()
    res = ''
    for j in s:
        if j not in 'aeiou':
            res += j
    
    print(f'#{i + 1} {res}')
