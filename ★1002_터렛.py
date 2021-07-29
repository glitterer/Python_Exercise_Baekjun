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
        if (r1+r2) == distance or abs(r1-r2) == distance:  # r1과r2가 만나는 지점 1군데에서 류가 있을 수 있다.
            print(1)
        elif (r1+r2) > distance and abs(r1-r2) < distance:  # r1+r2가 더 크다면 distance 직선기준으로 아래 위로 총 2군데 발생할 수 있다.
            print(2)
        else:
            print(0)


'''
시도 2에서 틀린 이유...
계산한 거리는 반지름으로 r1, r2(r1 > r2)

두 중심간의 거리를 d라고 가정할 때

두 점에서 만나는 경우
d != 0 and r1 - r2 < d < r1 + r2

한 점에서 만나는 경우
d != 0 and { r1+r2 = d (외접) r1-r2 = d(내접)}

한 점에서도 만나지 않을 경우
d = 0 and r1 - r2 != 0
d != 0 and r1 + r2 > d

무수히 많은 점에서 만날 경우
d = 0 and r1 - r2 = 0
면 됩니다.
'''



'''
# 시도2
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
        if (r1+r2) == distance or abs(r1-r2) == distance:  # r1과r2가 만나는 지점 1군데에서 류가 있을 수 있다.
            print(1)
        elif (r1+r2) > distance and abs(r1-r2) < distance:  # r1+r2가 더 크다면 distance 직선기준으로 아래 위로 총 2군데 발생할 수 있다.
            print(2)
        else:
            pass
'''

'''
# 시도1
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
'''
