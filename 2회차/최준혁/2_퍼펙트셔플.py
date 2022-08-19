# import sys

# sys.stdin = open("_퍼펙트셔플.txt")
# 카드 덱을 절반으로 나누고 나눈것들에서 교대로 카드를 뽑아 새로운 덱을 만든다.

T = int(input())

for t in range(1, T+1):
    N = int(input()) # 카드의 개수 ex) 6
    card = list(input().split()) # 카드의 이름 A B C D E
    # print(card)
    meridian = N // 2 # 카드를 절반으로 나눈 몫 ex) 3
    a = []
    idx = 1
    if N % 2 == 0: # N이 짝수일때 
        for i in range(N): # 0 1 2 3 4 5
            if i < meridian: # 0 1 2 (A B C)
                a.append(card[i]) # 카드를 추가 card[0] = A / card[1] = B / card[2] = C 
            else: # 3 4 5(D E F)
                a.insert(idx, card[i]) # 해당 인덱스에 삽입 A D B E C F
                idx += 2 # 인덱스 2씩 증가 1, 3, 5
    else: # N이 홀수일때
        for j in range(N):
            if j < meridian+1: # 먼저 놓는쪽에 1장 추가
                a.append(card[j])
            else:
                a.insert(idx, card[j])
                idx += 2

    print("#{}".format(t), *a) # 테스트 케이스와 a의 전체값 출력