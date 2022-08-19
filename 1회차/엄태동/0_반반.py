import sys

sys.stdin = open("_반반.txt")
TC=int(input())
dic={}
for i in range(TC):
    word=input()
    for j in range(len(word)):
        if word[j] not in dic:
            dic[word[j]]=1
        else:
            dic[word[j]]+=1
    if len(dic.keys()) ==2 and len(dic.values())==2:
        print(f'#{i+1} Yes')
        dic={}
    else:
        print(f'#{i+1} No')    
        dic={}