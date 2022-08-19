import sys

sys.stdin = open("_반반.txt")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    

    a = list(input())
    
    # if a[0] == a[1]:
    #     cnt = cnt + 1
    # elif a[0] == a[2]:
    #     cnt = cnt + 1
    # elif a[0] == a[3]:
    #     cnt = cnt + 1
    # elif a[1] == a[2]:
    #     cnt = cnt + 1
    # elif a[1] == a[3]:
    #     cnt = cnt + 1
    # print(cnt)
    # for i in a:
        
    #     if a.count(i) == 2:
    #         result = 'YES'
    #     elif a.count(i) != 2:
    #         result = 'NO'
    # print(f'#{test_case} {result}')
    for i in range(len(a)):             #처음에는 그저 그냥 count가 2만 나오면 될줄 알았지만, 그렇게 하면 no 다음 yes가 나와도 yes 처리를 해버리는거 같아서, no가 나오면 break 를 걸어 no로
                                        #고정해야 패스할수 있는 문제였던거 같다
        if a.count(a[i]) == 2:
            result = 'Yes'
        elif a.count(a[i]) != 2:
            result = 'No'
            break
    print(f'#{test_case} {result}')
        
        
      
        



