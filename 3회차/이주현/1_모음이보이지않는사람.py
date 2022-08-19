import sys

sys.stdin = open("_모음이보이지않는사람.txt")


T = int(input())

for t in range(1,T+1):
    letter = str(input())
    my_letter = ''

    for i in letter:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            my_letter += i

    print('#{} {}'.format(t,my_letter))

    


