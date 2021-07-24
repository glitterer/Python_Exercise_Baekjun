a = int(input())
for i in range(a):
    H, W, N = map(int, input().split())
    hundred = N % H
    if (hundred == 0):
        hundred = H * 100
        decimal = N // H
    else:
        hundred = (N % H) * 100
        decimal = N // H + 1
    print(hundred + decimal)


'''
# 틀렸다고 나오는 코드
a = int(input())
for i in range(a):
    H, W, N = map(int, input().split())
    hundred = int(N % H)
    decimal = int(N // H) + 1
    if (hundred == 0):
        hundred = H
        if(len(str(decimal)) == 1):
            print(f"{hundred}0{decimal}")
        else:
            print(f"{hundred}{decimal}")
    else:
        if(len(str(decimal)) == 1):
            print(f"{hundred}0{decimal}")
        else:
            print(f"{hundred}{decimal}")
'''
