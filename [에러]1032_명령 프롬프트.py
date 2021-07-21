N = int(input())  # 파일 이름의 갯수
string = [0]*N  #string을 input으로 받기 때문에(그리고 input은 문자열을 한 줄로 받는다.) *N이 필요하다.
same = list()
# 단어를 입력한다.
for i in range(N):
    string[i] = input()

# 단어들에서 같은 부분 찾기
for i in string[0]:  #기준이 되는 string을 첫 번재 입력 string으로 하도록 한다.
    cnt = 0
    num = 0
    n = 0
    for j in string[cnt+1]:  #string[0]과 비교를 통해서 같은 부분을 남긴다.
        #print(list(string[0][num]))
        if string[0][num] == j:
            same[n] = string[0][num]
            n=n+1
        elif string[0][num] != j:
            same[n] = '?'
        cnt=cnt+1
        num=num+1
print(same)
