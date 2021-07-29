# 백준 예제 입출력은 제대로 나오나 틀렸다고 계속 채점이 되는 중... 다시 확인 필요

test_case = int(input())  # 테스트 케이스 갯수

for i in range(test_case):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))  # 조규현 좌표(x1, y1)과 백승환 좌표(x2, y2)와 류재명과의 거리 r1, r2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if distance == 0:
        if r1 != r2:  # 류가 있을 수 있는 위치가 존재하지 않는다.
            print(0)
        else:  # 류가 있을 수 있는 위치는 r1(=r2)를 반지름으로 가진 원의 위치 중 어디든 가능하다.
            print(-1)
    else:
        if (r1+r2) == distance:  # r1과r2가 만나는 지점 1군데에서 류가 있을 수 있다.
            print(1)
        elif (r1+r2) > distance:  # r1+r2가 더 크다면 distance 직선기준으로 아래 위로 총 2군데 발생할 수 있다.
            print(2)
        else:
            pass
