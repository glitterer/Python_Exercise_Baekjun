tea_type = int(input())  #1~4
contestant_answers = list(map(int, input().split()))
# print(contestant_answers)
ans_cnt = 0
for i in contestant_answers:
    if i == tea_type:
        ans_cnt = ans_cnt + 1
print(ans_cnt)
