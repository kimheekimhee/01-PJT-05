# import sys

# sys.stdin = open("_반반.txt")

TC = int(input()) # 테스트 케이스의 수

for t in range(1, TC+1): # 1부터 테스트케이스 +1 까지
    S = input() # 입력
    ban = list(set(S)) # 입력값을 리스트에 셋으로 저장
    flag = True # 반반인지 확인할 변수

    for i in ban: # eeff -> e, f
        if S.count(i) != 2: # 2개가 안들어있으면
            flag = False # 반반아님
        
    if flag: # 참일시
        print("#{} {}".format(t, "Yes"))
    else:
        print("#{} {}".format(t, "No"))
