birth_pass = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
kor_age = int(input("한국 나이를 입력해주세오: "))
if birth_pass == 0:
    us_age = kor_age
    print(f"당신의 한국 나이는 {kor_age}살이고, 생일이 지났으므로 미국나이도 {us_age}살 입니다.")
elif birth_pass == -1:
    us_age = kor_age-1
    print(f"당신의 한국 나이는 {kor_age}살이고, 생일이 지나지 않았으므로 미국나이는 {us_age}살 입니다.")
else:
    print("생일이 지났는지에 대해서 0이나 -1을 입력하지 않았습니다.")
