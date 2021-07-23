def bus_fare(age, pay_type):
    if pay_type == "카드":
        if age < 8 or age >= 75:
            pay = "무료"
        elif age < 14:
            pay = "450"
        elif age < 20:
            pay = "720"
        elif age >= 20 and age < 75:
            pay = "1200"
        else:
            pass
    elif pay_type == "현금":
        if age < 8 or age >= 75:
            pay = "무료"
        elif age < 14:
            pay = "450"
        elif age < 20:
            pay = "1000"
        elif age >= 20 and age < 75:
            pay = "1300"
        else:
            pass
    return pay

age = int(input("나이를 입력하세요: "))
pay_type = (input("지불유형을 입력하세요(카드/현금): "))
bus_fare_res = bus_fare(age, pay_type)

#출력
print(f"나이: {age}세")
print(f"지불유형: {pay_type}")
print(f"버스요금: {bus_fare_res}원")
