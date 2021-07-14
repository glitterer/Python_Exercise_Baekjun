for i in range(0,int(input())):
    sum = 0
    num = int(input())
    for i in range(1, num+1):
        if i % 2 == 1:
            sum = sum + i
    print(sum)
