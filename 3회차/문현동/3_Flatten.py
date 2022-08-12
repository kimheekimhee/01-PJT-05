import sys

sys.stdin = open("_Flatten.txt")

for test_case in range(1, 11):
    dump_ = int(input())
    
    boxes = [*map(int, input().split())]
    
    # 박스들 중 제일 큰 값의 자리를 찾아서 제일 큰 값에 -1 을 한 값을 그 자리에 대신 넣고
    # 제일 작은 값의 자리를 찾아서 제일 작은 값에 +1 을 한 값을 그 자리에 대신 넣기
    
    i = 0
    while i < dump_: # 여기서 처음에 <= 를 해서 틀렸는데 < 를 해야 하는 이유는 하나 적을때 다시 들어가서 덤프와 같게 되니까 만약 <= 조건을 사용하려면 i = 1 로 했어야 했던 것 같다.
        boxes[boxes.index(max(boxes))] = boxes[boxes.index(max(boxes))] - 1
        boxes[boxes.index(min(boxes))] = boxes[boxes.index(min(boxes))] + 1
        i += 1
    
    print(f"#{test_case} {max(boxes) - min(boxes)}")