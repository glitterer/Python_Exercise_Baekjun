def rcp(my):
    if computer == 0:  #컴퓨터가 가위
        if my == "가위" or my == '0':
            print("나: 가위\n컴퓨터: 가위\n비겼습니다.")
        elif my == "바위" or my == '1':
            print("나: 바위\n컴퓨터: 가위\n사용자 승리!")
        elif my == "보" or my == '2':
            print("나: 보\n컴퓨터: 가위\n컴퓨터 승리!")
        else:
            pass
    elif computer == 1:  #컴퓨터가 바위
        if my == "가위" or my == '0':
            print("나: 가위\n컴퓨터: 바위\n컴퓨터 승리!")
        elif my == "바위" or my == '1':
            print("나: 바위\n컴퓨터: 바위\n비겼습니다")
        elif my == "보" or my == '2':
            print("나: 보\n컴퓨터: 바위\n사용자 승리!")
        else:
            pass
    elif computer == 2:  #컴퓨터가 보
        if my == "가위" or my == '0':
            print("나: 가위\n컴퓨터: 보\n사용자 승리!")
        elif my == "바위" or my == '1':
            print("나: 바위\n컴퓨터: 보\n컴퓨터 승리!")
        elif my == "보" or my == '2':
            print("나: 보\n컴퓨터: 보\n비겼습니다")
        else:
            pass
    else:
        pass

#입력
my = input("가위(0) 바위(1) 보(2) 중에 선택하세요(문자or숫자 선택): ")
print("가위 바위 보 게임을 시작합니다.")

#랜덤함수
import random
computer = random.randint(0, 2)

#출력을 위한 함수
rcp(my)
