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
        result.append(str(student_score[i]) + "," + student_name[i])
    result.sort(reverse=True)
    # print(result[-1][:3])
    for _ in range(len(result)):
        if result[-1][:3] == '100':  # sort에 의해 100점은 index 마지막자리에 있다.
            result.insert(0, result[-1])  # index 0에 100점을 추가시킨다.
            result.pop()  # 추가시킨 100을 마지막 자리에서 없앤다.
            continue
        else:
            break
    # print(result)

    # 동점일때와 100점일 때의 등수도 처리
    rank = []
    for i in range(len(student_name)):
        result[i].split(',')
        if result[i][:3] == '100':
            rank.append(1)
            print(f"학생: {result[i][4:]} 점수: {result[i][:3]}점 {rank[i]}등")
        else:
            if result[i-1][:2] == result[i][:2]:
                rank.append(i)
                print(f"학생: {result[i][3:]} 점수: {result[i][:2]}점 {rank[i]}등")
            else:
                rank.append(i+1)
                print(f"학생: {result[i][3:]} 점수: {result[i][:2]}점 {rank[i]}등")
        # print(result)


# 학생 답
s = ["김갑,3242524215",
     "이을,3242524223",
     "박병,2242554131",
     "최정,4245242315",
     "정무,3242524315",
     "실1,3242524312",
     "실2,3242524312",
     "실3,3242524315"]

# 정답지
a = [3, 2, 4, 2, 5, 2, 4, 3, 1, 2]

grader(s, a)
