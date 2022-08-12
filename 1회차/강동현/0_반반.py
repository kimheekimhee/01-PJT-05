import sys

sys.stdin = open("_반반.txt")

T = int(input())
dic = {}
for z in range(T):
    line = list(input())
    dic = sorted(line)
    if dic[0]==dic[1] and dic[2]==dic[3] and dic[1]!=dic[2]:
        print(f'#{z+1} Yes')
    else:
        print(f'#{z+1} No')