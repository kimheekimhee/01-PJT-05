import sys

sys.stdin = open("_등산로조성.txt")

dr = [-1,0,1,0] # 상 우 하 좌
dc = [0,1,0,-1]

def dfs(row,col,path,construct):
    global ans
    if ans < path: # 등산로 갱신
        ans = path
    for k in range(4): # 델타탐색
        nrow = row+dr[k]
        ncol = col+dc[k]
        if nrow<0 or nrow>=N or ncol<0 or ncol>=N:
            continue # 영역벗어나면 패스
        if visited[nrow][ncol] == 1:
            continue
        if mountain[row][col]>mountain[nrow][ncol]:
            visited[nrow][ncol] = 1 #이동가능하면
            dfs(nrow,ncol,path+1,construct) # 재귀호출
            visited[nrow][ncol] = 0 # 갔다오면 초기화
        elif mountain[row][col]<=mountain[nrow][ncol] and construct ==False: # 이동불가능하면
            for i in range(1,K+1):
                mountain[nrow][ncol]-=1 # 공사해보기
                construct = True
                if mountain[row][col]>mountain[nrow][ncol]:
                    visited[nrow][ncol] =1
                    dfs(nrow,ncol,path+1,construct)
                    visited[nrow][ncol] = 0
                construct = False # 다른경우 확인 위해
                mountain[nrow][ncol] += i # 공사 취소

T = int(input())
for z in range(T):
    N,K = map(int,input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    top = 0 # 정상 찾기
    for i in range(N):
        for j in range(N):
            if top < mountain[i][j]:
                top = mountain[i][j]
    ans = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == top: # 정상높이랑 같으면
                visited = [[0]*N for _ in range(N)]
                visited[i][j] = 1 
                dfs(i,j,1,False) # 등산로 탐색
    print(f'#{z+1} {ans}')