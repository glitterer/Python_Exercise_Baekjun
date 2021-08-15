# 정답 예시를 토대로 만들었습니다...
# 정답 예시를 한 번 봐버리니까 뇌리에서 사라지지 않더라구요.. ㅠ

def grader(student, answers):
    student_name = list()
    student_ans = list()
    student_score = list()
    result = list()
    for i in student:
        i = i.split(",")
        student_name.append(i[0])
        student_ans.append(i[1])
    # print(student_ans[0][8])
    for i in range(len(student_name)):
        score = 0
        for j in range(len(answers)):
            if int(answers[j]) == int(student_ans[i][j]):
                score += 10
        student_score.append(score)
    # print(student_score)

    for i in range(len(student_name)):
        result.append(str(student_score[i]) + student_name[i])
    result.sort(reverse=True)
    # print(result)

    for i in range(len(student_name)):
        print(f"학생: {result[i][2:4]} 점수: {result[i][:2]}점 {i + 1}등")


# 학생 답
s = ["김갑,3242524215",
     "이을,3242524223",
     "박병,2242554131",
     "최정,4245242315",
     "정무,3242524315"]

# 정답지
a = [3, 2, 4, 2, 5, 2, 4, 3, 1, 2]

grader(s, a)
