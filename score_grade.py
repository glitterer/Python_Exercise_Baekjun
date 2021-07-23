def grader(name, score):
    if score >= 95:
        grade = 'A+'
    elif score >= 90:
        grade = 'A'
    elif score >= 85:
        grade = 'B+'
    elif score >= 80:
        grade = 'B'
    elif score >= 75:
        grade = 'C+'
    elif score >= 70:
        grade = 'C'
    elif score >= 65:
        grade = 'D+'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

#입력
name = input("학생이름을 입력하세요: ")
score = int(input("점수를 입력하세요: "))
grade = grader(name, score)  #함수를 불러서 grade변수에 리턴값을 넣는다.

#출력
print("학생이름 : ", name, sep = '')
print("점수 : ", str(score) + "점", sep = '')
print("학점 : ", grade, sep = '')
