import sys

sys.stdin = open("_퍼펙트셔플.txt")
answer_list = []
T = int(input())
for _ in range(T):
    _ = input()
    data = input().split()
    if len(data)%2 == 0:
        n = len(data)//2 # 짝수면 사이좋게 반반 
    else:
        n = len(data)//2 + 1 # 홀수면 첫째에게 더 준다. 
    Card_deck_1 = data[:n] # 절반씩 분배 
    Card_deck_2 = data[n:]
    answer = []
    for i in range(len(data)):
        if i % 2 == 0:
            answer.append(Card_deck_1[i//2]) # 중간에 하나씩 섞어준다. 
        else:
            answer.append(Card_deck_2[i//2])
    answer_list.append(answer)
for t in range(T):
    print(f"#{t+1}",end=" ")
    print(*answer_list[t])