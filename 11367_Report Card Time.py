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

 '''
    repeat = int(input())
for i in range(0, repeat):
    name, score = input().split()  # 이 부분이 중요. 2개 이상 입력받기를 계속 햇갈리는 중...2021-7-16
    # print(name, score, sep=' ')
    score = int(score)  # 이렇게 하나만 넣으면 score는 int형으로 변환이 된다.
    if score >= 97:
        grade = "A+"
    elif score <= 96 and score >= 90:
        grade = "A"
    elif score <= 89 and score >= 87:
        grade = "B+"
    elif score <= 86 and score >= 80:
        grade = "B"
    elif score <= 79 and score >= 77:
        grade = "C+"
    elif score <= 76 and score >= 70:
        grade = "C"
    elif score <= 69 and score >= 67:
        grade = "D+"
    elif score <= 66 and score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(name, grade, sep=' ')
'''
