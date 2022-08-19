import sys

sys.stdin = open("_반반.txt")

S = int(input())
dic = {}
for i in range(S):
    line = list(input())
    dic = sorted(line)
    if dic[0]==dic[1] and dic[2]==dic[3] and dic[1]!=dic[2]:
        print(f'#{i+1} Yes')
    else:
        print(f'#{i+1} No')
