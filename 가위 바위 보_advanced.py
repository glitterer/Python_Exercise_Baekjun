'''
가위 바위 보 게임
조건 1: 게임을 몇 판을 진행할 것인지 입력을 받아주기
조건 2: 0, 1, 2, "가위", "바위", "보" 이외에 다른 입력을 받으면 재입력 받기
조건 3: 게임종료 후 나와 컴퓨터의 총 전적 출력하기
'''
import random

def rsp_advanced(games):
    game_rounds = 1
    win = 0
    tie = 0
    lose = 0
    while(game_rounds <= games):  # 게임을 game_rounds의 수만큼 한다.
        while True:
            player = input("가위(0), 바위(1), 보(2) 중에 선택하세요 : ")
            rps_number = rps_to_number(player)
            if rps_number == -1:
                print("잘못 입력하셨습니다.")
                continue
            else:
                break
        result, com_value = com_vs_player(rps_number)
        printout(rps_number, result, com_value, game_rounds, win)
        if result == 1:
            tie += 1
            print(f"{game_rounds} 번째 판은 무승부! \n")
        elif result == 0:
            lose += 1
            print(f"{game_rounds} 번째 판은 컴퓨터의 승리! \n")
        elif result == 2:
            win += 1
            print(f"{game_rounds} 번째 판은 나의 승리! \n")
        game_rounds += 1
    print(f"나의 전적: {win}승 {tie}무 {lose}패")
    print(f"컴퓨터의 전적: {lose}승 {tie}무 {win}패")


# "가위", "바위", "보"를 숫자로 변환
def rps_to_number(player):
    if player == "가위" or player == '0':
        number_to_rps = 0
    elif player == "바위" or player == '1':
        number_to_rps = 1
    elif player == "보" or player == '2':
        number_to_rps = 2
    else:
        number_to_rps = -1
    return number_to_rps


def com_vs_player(rps_number):
    computer = random.randint(0, 2)  # 랜덤함수
    if computer == rps_number:  #비겼을 경우
        return 1, computer
    elif (computer - rps_number) % 3 == 2:  # 이겼을 경우(computer - my == -1 or computer ==2 and my == 0)
        return 2, computer
    else:  # 졌을 경우
        return 0, computer


def printout(rps_number, result, com_value, game_rounds, win):
    if rps_number == 0:
        print("나: 가위")
    elif rps_number == 1:
        print("나: 바위")
    else:
        print("나: 보")

    if com_value == 0:
        print("컴퓨터: 가위")
    elif com_value == 1:
        print("컴퓨터: 바위")
    else:
        print("컴퓨터: 보")


# 몇 번 게임을 할 것인지 입력
games = int(input("몇 판을 진행하시겠습니까? : "))
rsp_advanced(games)
