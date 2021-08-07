def wrong_guest_book(guest_book):
    text_save = open("Q3_content.txt", "w", encoding="UTF8")   # 파일을 쓸 수 있도록 연다
    text_save.write(guest_book)   # 파일에 text를 쓴다.
    text_save.close()   # 파일을 닫는다.

    # 파일을 읽을 수 있도록 연다.
    file_read = open("Q3_content.txt", "r", encoding="UTF8")
    for line in file_read:
        name_phone = line.split(',')  # split()으로 콤마(,)를 기준으로 나눈다.
        name = name_phone[0].strip()  # strip()이 없으면 계속 잘못된 결과값 출력
        phone = name_phone[1].strip()
        # endswith(끝나는문자, 문자열의시작, 문자열의끝)
        # startswith(시작하는문자, 시작지점)
        if len(phone) != 13 \
        or phone.startswith("010") == False \
        or phone.endswith("-", 3, 4) == False \
        or phone.endswith("-", 8, 9) == False:
            print(f"잘못 쓴 사람: {name}")
            print(f"잘못 쓴 번호: {phone}\n")
        else:
            pass


guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""
wrong_guest_book(guest_book)
