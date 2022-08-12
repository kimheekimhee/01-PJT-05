# 미해결문제

import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

for _ in range(1, T+1):
    N, M = map(int, input().split())
    town = []

    for k in range(M):
        man1, man2 = input().split()
        
        if k == 0:
            town.append([man1, man2])
        else:
            for i in range(len(town)):
                for j in range(len(town[i])):
                    if (man1 in town[i] or man2 in town[i]):
                        town[i].append(man1)
                        town[i].append(man2)
                        break
                    else:
                        town.append([man1, man2])
                        break
            
            print(town)
    print("최종")
    print(town)
    print("--------------------------------------------------------------")