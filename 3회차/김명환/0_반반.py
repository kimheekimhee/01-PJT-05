import sys
sys.stdin = open("_반반.txt")

TC = int(input())
li = []
for i in range(TC):
    word = input()
    if len(set(word)) == 2:
        print(f'#{i+1} Yes')
    else:
        print(f'#{i+1} No')
            

