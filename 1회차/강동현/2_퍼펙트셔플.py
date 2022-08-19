import sys

sys.stdin = open("_퍼펙트셔플.txt")

from collections import deque

T = int(input())
for z in range(T):
    N = int(input())
    if N %2 == 0:
        mid = int(N/2)
        deck = list(input().split())
        Front = deque(deck[:mid])
        End = deque(deck[mid:])
        new = []
        while len(Front)!=0 and len(End)!=0:
            new.append(Front[0])
            Front.popleft()
            new.append(End[0])
            End.popleft()
        line = ' '.join(new)
        print(f'#{z+1} {line}')
    else:
        mid = int(N//2+1)
        deck = list(input().split())
        Front = deque(deck[:mid])
        End = deque(deck[mid:])
        new = []
        while len(Front)!=0 and len(End)!=0:
            new.append(Front[0])
            Front.popleft()
            new.append(End[0])
            End.popleft()
        new.append(deck[mid-1])
        line = ' '.join(new)
        print(f'#{z+1} {line}')
