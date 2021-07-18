str_len = int(input())
str = list(input())
# print(str[1])
cnt_2 = 0
cnt_e = 0
for i in range(str_len):
    if str[i] == '2':  # 여기서 계속 문제가 발생했었다.. list index out of range계속 발생 --> 이유.. for문의 range에서 str_len+1로 처리를 했었다...
        cnt_2 = cnt_2 + 1
    elif str[i] == 'e':
        cnt_e = cnt_e + 1
if cnt_2 > cnt_e:
    print(2)
elif cnt_2 < cnt_e:
    print('e')
else:
    print("yee")
