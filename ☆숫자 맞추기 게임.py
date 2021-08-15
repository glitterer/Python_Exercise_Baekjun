import random
import copy


def guess_numbers():
    three_numbers = []
    used_num = []
    trial = 1
    got_right = 0
    while len(three_numbers) < 3:
        rand_num = random.randint(0, 100)
        if rand_num not in three_numbers:
            three_numbers.append(rand_num)
        else:
            continue

    three_numbers.sort()
    # 최댓값을 먼저 찾아서 중간값이 최댓값으로 처리되는 것을 방지하기 위한 코드(line31~42)
    three_numbers_compare = copy.copy(three_numbers)
    # print(three_numbers)

    while got_right < 3:
        print(f"{trial}차 시도")
        guess_num = int(input("숫자를 예측해보세요: "))
        used_num.append(guess_num)
        # 만약 이미 예측해본 숫자에 대한 예외처리
        # print(used_num)
        if guess_num in used_num[:-1]:
            print("이미 예측에 사용한 숫자입니다.")
            used_num.pop()
            continue
        else:
            if guess_num in three_numbers:
                if guess_num == three_numbers_compare[2]:
                    print(f"숫자를 맞추셨습니다! {guess_num}는 최댓값입니다.")
                    three_numbers.pop()  # sort()를 통해서 정렬한 three_numbers 중에서 index가 가장 큰(=최댓값)을 pop
                elif guess_num == three_numbers_compare[0]:
                    print(f"숫자를 맞추셨습니다! {guess_num}는 최솟값입니다.")
                    three_numbers.pop(0)  # sort()를 통해서 정렬한 three_numbers 중에서 index가 가장 작은(=최솟값)을 pop
                else:
                    print(f"숫자를 맞추셨습니다! {guess_num}는 중간값입니다.")
                    three_numbers.remove(guess_num)  # remove()는 특정 값(value)을 list에서 뺄 수 있는 기능이다.
                got_right += 1
                trial += 1

            else:
                print(f"{guess_num}는 없습니다.")
                # 5회, 10회까지 정답을 못맞추면 최솟값, 최대값에 대한 힌트를 줍니다.
                if trial == 5:
                    if guess_num > three_numbers_compare[0]:
                        print(f"최솟값은 {guess_num}보다 작습니다")
                    else:
                        print(f"최솟값은 {guess_num}보다 큽니다")
                elif trial == 10:
                    if guess_num > three_numbers_compare[2]:
                        print(f"최댓값은 {guess_num}보다 작습니다")
                    else:
                        print(f"최댓값은 {guess_num}보다 큽니다")
                else:
                    pass
                trial += 1
    print("\n게임 종료")
    print(f"{trial - 1}번 시도만에 예측 성공")


print('=' * 30)
print("\t  숫자 맞추기 게임 시작!")
print('=' * 30)
guess_numbers()
