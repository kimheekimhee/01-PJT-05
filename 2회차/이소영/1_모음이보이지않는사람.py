import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t = int(input())

#word를 입력 받은 후 for문으로 돌면서 자음만 not_mo에 추가해 not_mo를 출력

for t in range(1, t+1): 
    word = input()
    not_mo = ''
    for i in word:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            not_mo += i

    print(f'#{t} {not_mo}')