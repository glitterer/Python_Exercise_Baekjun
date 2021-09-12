# 틀린 이유: B<=10이라는 조건이 있는데, 이에 맞게 출력이 되지 않는다.
num = list(map(int, input()))
a = []
b = []
for i in range(len(num)):
    if i != (len(num)-1):
        a.append(str(num[i]))
    else:
        b.append(str(num[i]))
print(int("".join(a))+int("".join(b)))
