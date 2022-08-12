import sys

sys.stdin = open("_Flatten.txt")

#tc = 10
#가장 큰 값을 가장 작은 값에 올려놓기

for i in range(10): #테스트 케이스만큼 반복
    d = int(input())  #dump 횟수
    box = list(map(int,input().split()))  #box 리스트

    for j in range(d): #dump만큼 반복

        max_index = box.index(max(box)) #최대 인덱스
        min_index = box.index(min(box)) #최소 인덱스
    # print(max_index)
    # print(min_index)
        box[max_index] -= 1 #최대 인덱스에서 1 빼기  -> 원래 9-1에서 8-2로 변했기 때문에
        box[min_index] += 1 #최대 인덱스에서 1 더하기
    
    print(f'#{i+1} {(max(box)-min(box))}')





