import sys

sys.stdin = open("_모음이보이지않는사람.txt")

# mo = ['a', 'e', 'i', 'o', 'u']

mo = "aeiou"

t = int(input())

for _ in range(t):
    s = input()

    for i in s:
        if i in mo:
            s = s.replace(i, '')

    print(f'#{_+1} {s}')


            
    
    


    