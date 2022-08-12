import sys

sys.stdin = open("_퍼펙트셔플.txt")
T=int(input())
stack=[]
for i in range(T):
    N=int(input())
    Card=input().split()
    if len(Card)%2==0:
        print(f'#{i+1} ', end='')
        for j in range(len(Card)//2):
            print(Card[j], end=' ')
            print(Card[len(Card)//2+j], end=' ')
    if len(Card)%2 != 0:
        Card2=list(reversed(Card))
        for k in range((len(Card)-1)//2):
            stack.append(Card2[k])
        print(f'#{i+1} ',end='')
        for m in range((len(Card)+1)//2):
            if stack ==[]:
                print(Card[m], end=' ')
            else:
                pop=stack.pop()
                print(Card[m], end=' ')
                print(pop, end=' ')
    print('')