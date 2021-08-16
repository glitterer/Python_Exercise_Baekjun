def after_100(month, date, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_list = ["월", "화", "수", "목", "금", "토", "일"]
    remaining_date_list = []
    hundred_days = 100  # 100일
    remaining_date_list.append(100)  # 시작 월에 남은 일수 list에 추가(추후 month index처리를 위해서)
    cur_month_list = month_list[month - 1]  # 시작 월의 index의 value
    remaining_initial_date = cur_month_list - date + 1  # 시작 월에 남은 일수("오늘부터 1일"=오늘 포함)
    remaining_date = hundred_days - remaining_initial_date  # 시작 월 제외하고 남은 일수
    remaining_date_list.append(remaining_date)  # 남은 일수를 list에 추가

    # 날짜 계산
    i = 0
    while True:
        if remaining_date > 0:
            i += 1
            month_index = (month - 1 + i) % 12
            remaining_date = remaining_date - month_list[month_index]  # 남은 날짜에 연속되는 달의 날짜를 차감
            remaining_date_list.append(remaining_date)  # 남은 일수를 list에 추가
        else:
            break
    # print(remaining_date_list)
    # 최종 월/일 계산
    final_date = remaining_date_list[-2]  # 100일 후 며칠 = list에서 가장 마지막 양수
    final_month = (month - 1 + len(remaining_date_list) - 1) % 12  # month 자기 자신 포함하니까 -1이고, len에서 음수를 빼면 -1
    if final_month == 0:
        final_month = 12
    # print(final_month, final_date)

    # 요일 계산
    day_index = day_list.index(day)  # index()를 통해 특정 원소의 위치를 찾을 수 있다.
    day_cal = 100 % 7  # 결과값: 2
    # 시작 날짜가 일요일이면 최종날짜는 월요일이 나오게 된다.
    if day_index != 6:
        final_day = day_list[day_index + day_cal - 1]
    else:
        final_day = "월"  # day_list[day_index + day_cal - 1 - len(day_list)]로 처리해도 된다

    print(f"{month}월 {date}일 {day}요일부터 100일 뒤는 {final_month}월 {final_date}일 {final_day}요일")


# 6월 21일 월요일부터 100일 뒤는 9월 28일 화요일
after_100(6, 21, "월")
# 9월 17일 일요일부터 100일 뒤는 12월 25일 월요일
after_100(9, 17, "일")
# 12월 25일 목요일부터 100일 뒤는 4월 3일 금요일
after_100(12, 25, "목")
# 2월 28일 일요일부터 100일 뒤는 6월 7일 월요일
after_100(2, 28, "일")
# 8월 28일 일요일부터 100일 뒤는 12월 5일 월요일
after_100(8, 28, "일")
# 10월 25일 일요일부터 100일 뒤는 2월 1일 월요일
after_100(10, 25, "일")
# 10월 25일 일요일부터 100일 뒤는 2월 1일 월요일
after_100(8, 20, "일")
