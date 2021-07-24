while True:
    tri = list(map(int, input().split()))
    sorted_tri = sorted(tri)
    if sorted_tri[0] == 0 or sorted_tri[1] == 0 or sorted_tri[2] == 0:  # 마지막 줄에 주어지는 입력 케이스이다: 0 0 0
        break
    else:
        pass

    if(sorted_tri[0]**2 + sorted_tri[1]**2) == sorted_tri[2]**2:
        print("right")
    else:
        print("wrong")
