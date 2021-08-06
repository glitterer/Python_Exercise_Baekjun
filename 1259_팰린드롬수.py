while True:
    flag = 1  # 숫자 하나만 들어갈 경우, yes로 처리하기 위해서 1로 초기화
    num = list(input())
    if num[0] == '0':
        break
    else:
        for i in range(len(num)//2):
            if num[i] == num[len(num)-1-i]:
                flag = 1
            else:
                flag = 0
                break  # 1223 같은 수를 위해서 반드시 필요
        if flag == 1:
            print("yes")
        else:
            print("no")
