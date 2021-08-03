num = int(input())
score = list(map(int, input().split()))
max_score = max(score)
sum = 0

for i in range(num):
    score[i] = score[i] / max_score * 100

for i in range(num):
    sum = sum + score[i]
average = sum/num

print(average)
