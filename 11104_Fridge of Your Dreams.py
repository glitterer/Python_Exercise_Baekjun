# 파이썬에서는 binary를 input으로 입력을 받고, 이를 int를 통해서 binary변수의 수를 밑이 2인 것으로 하여 변환이 가능하다.
for i in range(0, int(input())):
    binary = input()
    print(int(binary, 2))  # 밑(2가 있는 자리)을 어떤 수로 해서 처리할 것인지 
