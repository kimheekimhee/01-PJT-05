import sys
from pprint import pprint
sys.stdin = open("_등산로조성.txt")
T=int(input())
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(T):
    N,K=map(int, input().split())
    Matrix=[list(map(int,input().split())) for _ in range(N)]
    if i==0:
        pprint(Matrix)
    max_=0
    index=[]
    index_list=[]
    stack=[]                            # K 깊이 만큼 판 뒤 길이 구하기 위해 인덱스 값을 튜플 형태로 stack할 생각
    for j in range(len(Matrix)):        #for문을 통한 max값 추출
        for k in range(len(Matrix)):
            if max_ <= max(Matrix[j]):
                max_=max(Matrix[j])
    for j in range(len(Matrix)):        #for문을 통한 max값에 해당하는 index 추출
        for k in range(len(Matrix)):
            if max_==Matrix[j][k]:
                index.append(j)
                index.append(k)
                index_list.append(index)
                index=[]
    if i ==0:
        print(index_list)
    for i in range(len(index_list)):    #가장 높은 곳에서 시작하는 row, column 설정
        row= index_list[i][0]
        column= index_list[i][1]
        path_length=0
        No=0                
        while 1:
           
            if No==4:          # 모든 방면으로 이동 불가능할때 
                break
            else:
                No=0
            next_path=0
            for j in range(4):              # 가로,세로 길 찾기, 그 다음으로 큰 값의 길 찾기
                if 0<=row+dx[j]<=N-1 and 0<=column+dx[j]<=N-1:
                    if next_path<=Matrix[row+dx[j]][column+dy[j]]<Matrix[row][column]:
                        next_path=Matrix[row+dx[j]][column+dy[j]]
                        stack.append((next_path,row+dx[j],column+dy[j]))
                    else:
                        No+=1
            for _ in range(len(stack)):
                tuple=stack.pop()
                if tuple[0]==next_path:
                    row=tuple[1]
                    column=tuple[2]
                    path_length+=1
                    break
    print(path_length)                
            # for k in range(K):          # next_path에 대해 깊이를 0~K까지 