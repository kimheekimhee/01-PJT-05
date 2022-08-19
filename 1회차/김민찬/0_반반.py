import sys

sys.stdin = open("_반반.txt")

TC = int(input())
for tc in range(1, TC + 1):
    S = list(input()) # 문자열 S가 주어진다.
    end = False # 종료 확인용 end
 
    for i in S:
        if S.count(i) == 2: # count 값이 2이면 pass
            pass
        else:
            end = True # count 값이 2가 아니면 end를 True로 바꾸고
            break # for문 종료
  
    if end == True:
        print('#{} {}'.format(tc, 'No'))
    else:
        print('#{} {}'.format(tc, 'Yes'))