import sys

sys.stdin = open("_창용마을무리의개수.txt")
sys.setrecursionlimit(10000)                # 재귀함수 횟수제한 늘림
input = sys.stdin.readline

T = int(input())                            # 테스트케이스 개수

for test_case in range(1, T+1):
    N, M = map(int, input().split())        # 사람(정점), 관계(간선) 수

    village = [[] for i in range(N+1)]      # 창용 마을 인접 리스트
    for i in range(M):                      # M개의 관계
        p1, p2 = map(int, input().split())  # 관계가 있는 두 사람
        village[p1].append(p2)              # 인접하므로 정점 추가
        village[p2].append(p1)              # 무방향이므로 반대도 추가
    
    people = [0] * (N+1)                    # 모든 마을 사람 확인, 초기값 0
    def connect(p):                         # 시작 사람 번호를 받는 함수
        people[p] = 1                       # 확인했으므로 1로 변경
        for i in village[p]:                # 해당 사람과 관계가 있는 사람들
            if people[i] == 0:              # 확인하지 않았으면
                connect(i)                  # 연결된 사람들의 관계까지 순회

    team = 0                                # 무리 수
    for i in range(1, N+1):                 # 1번부터 N번까지의 사람들
        if people[i] == 0:                  # 확인되지 않은 사람이면
            team += 1                       # 새로운 무리 시작이므로 +1
            connect(i)                      # 해당 사람부터 순회 시작

    print(f'#{test_case} {team}')           # 무리 수 출력