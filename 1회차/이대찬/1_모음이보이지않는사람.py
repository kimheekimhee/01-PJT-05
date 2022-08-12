import sys

sys.stdin = open("_모음이보이지않는사람.txt")

N = int(input())

alp = 'aeiou'
for i in range (1,N+1):
    string  = input()
    for n in alp:
        string = string.replace(n, '')
    print(f'#{i} {string}')
    
    