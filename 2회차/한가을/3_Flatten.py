import sys

sys.stdin = open("_Flatten.txt")

# 한 쪽 벽면에 노란색 상자들이 쌓여있다
# 높은 곳의 상자를 낮은 곳에 옮기는 방식으로
# 최고점과 최저점의 간격을 줄이는 작업을 평탄화 작업이라고 함
# 평탄화를 모두 수행하고 나면 가장 높은 곳과 낮은 곳의 차이가 최대 1 이내
# 상자를 옮기는 작업 횟수에 제한이 걸려있을 때
# 제한된 횟수만큼 옮기는 작업을 한 후
# 최고점과 최저점의 차이를 반환하는 프로그램

# 가로 길이는 항상 100
# 모든 위치에서 1 <= boxHeight(상자의 높이) <= 100
# 1 <= dumpsNumber(덤프 횟수) <= 1000

# 총 10개의 테스트 케이스가 주어지면
# 각 테스트 케이스의 첫 번째 줄에 덤프 횟수가 주어진다
# 다음 줄에 각 상자의 높이값이 주어진다

# #부호와 함께 테스트 케이스의 번호를 출력하고
# 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차 출력

# 출력 예시
#1 13
#2 32
#3 54
#4 25
#5 87
#6 14
#7 39
#8 26
#9 13
#10 29

for tc in range(1, 10 + 1):
    #* 덤프 횟수
    dumpsNumber = int(input())
    #* 박스 높이
    boxHeight = list(map(int, input().split()))

    #* 층마다 몇개가 있는지 세기
    count = [0] * 101
    for i in boxHeight:
        count[i] += 1

    #* 1 <= 상자 높이 <= 100 이니까
    min = 101
    max = 0
    for box in boxHeight:
        if box < min:
            min = box
        elif box > max:
            max = box

    #* max 높이에서 1개 빼고 그 값을 min 높이에 더함 -> 카운팅 변경
    #* 덤프 횟수만큼 반복문 돌리기
    #* 단, min, max 높이가 달라지므로 같이 체크
    n = 0
    while n < dumpsNumber:
        count[max] -=1
        count[max - 1] += 1
        count[min] -= 1
        count[min + 1] += 1

        #* max, min 높이인 것들의 개수가 0개면 안됨
        #* 따라서 0이 아닐 때까지 찾아서 값 변경
        while count[max] == 0:
            max -= 1
        while count[min] == 0:
            min += 1
        
        #* while문 탈출을 위해 1씩 더함
        n += 1
    result = max - min

    print('#{} {}'.format(tc, result))