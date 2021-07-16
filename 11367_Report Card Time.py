repeat = int(input())
for i in range(0, repeat):
    name, score = input().split()  # 이 부분이 중요. 2개 이상 입력받기를 계속 햇갈리는 중...2021-7-16
    # print(name, score, sep=' ')
    if int(score) >= 97:
        grade = "A+"
    elif int(score) <= 96 and int(score) >= 90:
        grade = "A"
    elif int(score) <= 89 and int(score) >= 87:
        grade = "B+"
    elif int(score) <= 86 and int(score) >= 80:
        grade = "B"
    elif int(score) <= 79 and int(score) >= 77:
        grade = "C+"
    elif int(score) <= 76 and int(score) >= 70:
        grade = "C"
    elif int(score) <= 69 and int(score) >= 67:
        grade = "D+"
    elif int(score) <= 66 and int(score) >= 60:
        grade = "D"
    else:
        grade = "F"
    print(name, grade, sep=' ')
