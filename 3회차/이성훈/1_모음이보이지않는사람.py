import sys

sys.stdin = open("_모음이보이지않는사람.txt")

word_ = ['a', 'e', 'i', 'o', 'u']

T = int(input())

for j in range(1, T+1):
    data = input()


    for i in word_:
        if i in data:
            data = data.replace(i, '')
            
    print(f'#{j} {data}')