import sys

sys.stdin = open("_Flatten.txt")
answer_list = []

for _ in range(10):
    N = int(input()) # 횟수

    data = list(map(int,input().split()))

    data.sort() # 우선 정렬을 시키고 
    
    for _ in range(N):
        for i in range(100):
            if data[i] <= data[i+1]: # 이상무
                break
            else:
                a = data[i] # 맨 앞이 최소값이 아니면 뒤로 보낸다. 
                b = data[i+1]
                data[i] = b
                data[i+1] = a
        for i in range(99,0,-1):
            if data[i] >= data[i-1]: # 이상무
                break
            else:
                a = data[i] # 맨 앞이 최대값이 아니면 앞으로 보낸다. 
                b = data[i-1]
                data[i] = b
                data[i-1] = a       
        data[0] += 1 # 맨앞에 플1
        data[-1] -= 1 # 맨 뒤에 마1
    answer_list.append(max(data)-min(data)) # 혹시 식에 오류가 있을까봐 max랑 min이랑 써 줘서 차를 구했습니다. 
for ans in range(10):
    print(f"#{ans+1} {answer_list[ans]}")

    