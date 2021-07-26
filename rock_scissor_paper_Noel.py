#Noel님 코드
def str(number):
    if number==0:
        return "가위"
    elif number==1:
        return "바위"
    elif number==2:
        return "보"
    elif number==3:
        return "당신의 승리!"
    elif number==4:
        return "컴퓨터 승리!"
    elif number==5:
        return "비겼습니다!"

def rcp(mine):
    try:
        if mine == "가위":
            mine = 0
        elif mine == "바위":
            mine = 1
        elif mine == "보":
            mine = 2
        else :
            mine = int(mine)
            if mine<0 or mine>2:
                quit()
    except:
        print('오타입니다. 다시 실행하세요.')
        quit()

    if computer < mine :
        if mine-computer == 1 :
            vic = 3
        else :
            vic = 4
    elif mine < computer :
        if computer - mine == 1 :
            vic = 4
        else :
            vic = 3
    else :
        vic = 5

    print("나:", str(mine))
    print("컴퓨터:", str(computer))
    print(str(vic))

import random
computer = random.randint(0,2)
print('가위(0) 바위(1) 보(2) 중 하나를 선택하세요.')
mine= input("Enter your choice: ")

rcp(mine)
