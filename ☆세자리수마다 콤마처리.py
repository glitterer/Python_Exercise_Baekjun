# f"{숫자:,}"  # 세 자리수마다 나누기
# print(f"{1000:,}")
def make_comma(num):
    num_list = list(str(num))  # list형으로 숫자를 변환한다.
    num_list_reverse = num_list[::-1]  # list형의 숫자들을 역순으로 한 배열 생성
    res = []  # 결과를 넣을 배열
    for i in range(len(num_list)):  # 자릿수의 숫자만큼 반복한다.
        if i % 3 == 0 and i != 0:   # 3씩 나눴을 때 일의자리 빼고 콤마(,)삽입
             res.append(',')  # 결과배열에 삽입시킨다.
        res.append(num_list_reverse[i])  # 한 번 반복마다 자릿수의 숫자 삽입
    for i in res[::-1]:  # 역순으로 되어있는 결과배열을 다시 역순으로 하고 반복
        print(i, end='')    # 숫자 출력


make_comma(100)
