import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
 
for tc in range(1,1+T):
    word = str(input())
    a = ''
 
    for q in word:
        if q != 'a' and q != 'e' and q != 'i' and q != 'o' and q != 'u':
            a += q
 
    print('#{} {}'.format(tc,a))