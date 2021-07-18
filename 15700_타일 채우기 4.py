N, M = input().split()
print(int(int(N)*int(M)/2))
# //연산자는 파이썬에서 나누기 연산 후, 소수점 이하의 수를 버리고 정수 부분의 수만 구한다.
print(int(int(N)*int(M)//2))  #이게 현 문제의 정답
