def check_id(id_number):
    while True:
        gender = ""
        # 주민등록번호는 6자리 이후에 -로 구분되어야 하고 길이는 -포함 14임
        if len(id_number) != 14 or id_number.endswith("-", 6, 7) == False:
            print("잘못된 번호입니다.")
            break
        # 00 ~ 21로 시작할 경우 2000년 이후 출생자인지 물어 볼 것 (맞으면 o 틀리면 x)
        if int(id_number[:2]) >= 0 and int(id_number[:2]) <= 21:
            ask = input("2000년 이후 출생자인가요? 맞으면 o 틀리면 x를 입력해주세요: ")
            if ask == 'o':  # 뒷자리 3, 4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음
                if id_number.endswith('3') == True:
                    gender = "남자"
                elif id_number.endswith('4') == True:
                    gender = "여자"
                else:
                    print("잘못된 번호입니다.")
            else:  # 1900 ~ 1921년 출생
                if id_number.endswith('1') == True:
                    gender = "남자"
                elif id_number.endswith('2') == True:
                    gender = "여자"
                else:
                    print("잘못된 번호입니다.")
        else:  # 1922~1999 출생
            if id_number.endswith('1') == True:
                gender = "남자"
            elif id_number.endswith('2') == True:
                gender = "여자"
            else:
                print("잘못된 번호입니다.")
        # 마무리 출력
        year = id_number[:2]
        mon = id_number[2:4]
        if gender == "남자" or gender == "여자":
            print(f"{year}년 {mon}월 {gender}\n")
        else:
            print("올바른 번호를 넣어주세요\n")
        break

a = "500629-2222222"
check_id(a)
# 50년06월 여자

a = "000629-2222222"
check_id(a)
# 2000년 이후 출생자 입니까? 맞으면 o 아니면 x : o
# 잘못된 번호입니다.
# 올바른 번호를 넣어주세요

a = "000629-2222222"
check_id(a)
# 2000년 이후 출생자 입니까? 맞으면 o 아니면 x : x
# 00년06월 여자
