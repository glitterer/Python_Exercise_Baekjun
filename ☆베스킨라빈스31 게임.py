def bs31():
    import random
    current_number = 0  # 현재 숫자
    while True:
        # list(map(int, input().split()))을 통해서 input값을 빈칸을 구분자로 하여 int형으로 받아서 list로 저장하라는 뜻이다.
        player = list(map(int, input("Player는 숫자를 입력하세요: ").split()))
        # player는 숫자 3개까지만 입력이 가능하다
        if len(player) > 3:
            print("숫자는 3개까지만 입력이 가능합니다.")
            continue
        # 숫자는 이전 값(=현재 숫자) 보다 1만큼 큰 숫자로 시작해야 한다.
        if player[0] != current_number + 1:
            print("이전의 숫자보다 1만큼 큰 숫자로 시작해야 합니다.")
            continue
        # 숫자는 연속적으로 입력되어야 한다.
        if len(player) == 3:
            if player[2] - player[1] != 1 or player[1] - player[0] != 1:
                print("연속된 숫자가 입력되어야 합니다.")
                continue
            else:
                current_number = player[2]
        elif len(player) == 2:
            if player[1] - player[0] != 1:
                print("연속된 숫자가 입력되어야 합니다.")
                continue
            else:
                current_number = player[1]
        elif len(player) == 1:
            current_number = player[0]

        # 현재 숫자는 player 리스트의 가장 끝 index에 해당하는 정수값이다.
        current_number = player[-1]
        print(f"현재 숫자 : {current_number}")

        # player가 31 이상의 숫자를 선택할 시에 패배한다.
        if current_number >= 31:
            print("\nPlayer가 패배했습니다.")
            break

        # 현재 숫자에서 31이 되기까지 남은 차례를 remaining_turn이다. line 52에서 사용된다.
        remaining_turn = 31 - current_number
        computer = list()
        computer_turn = random.randint(1, 3)
        for i in range(computer_turn):
            current_number += 1
            computer.append(current_number)
            # 컴퓨터 입장에서 승리를 하기 위해서 31 이전의 숫자까지 선택한다.
            # 하지만 31밖에 선택지가 없으면 31을 선택 후 끝낸다.
            if current_number >= 31:
                print(f"컴퓨터 : 31")
                break
            if computer_turn <= remaining_turn:
                print(f"컴퓨터 : {current_number}")
                continue
        print(f"현재 숫자 : {current_number}\n")

        # 컴퓨터가 31을 선택할 시에 player의 승리
        if computer[-1] == 31:
            print("Player가 승리했습니다.")
            break


# 숫자 게임을 시작하자
print('=' * 30)
print("\t베스킨라빈스31 게임 시작!")
print('=' * 30)
bs31()
