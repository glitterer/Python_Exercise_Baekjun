A = ['SUN','MON','TUE','WED','THU','FRI','SAT'] #1
B = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #2

X, Y = map(int, input().split()) #3
Day = 0
for i in range(0,X-1) : #4 
    Day += B[i]

Day = (Day + Y) % 7 #5

print(A[Day]) #6

'''
https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-1924%EB%B2%88-2007%EB%85%84-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

- #1 : 요일에 대한 리스트

- #2 : 월에 따른 일자 리스트

- #3 : 월과 일 입력

- #4 : 리스트는 0부터 시작하기 때문에 범위는 0,X-1로 설정하고, 요일을 구하는 방법은 Day를 다 더해서 7로 나누면 요일이 나오기 때문에 데이를 다 더한다.

- #5 : 더한 Day를 7로 나누기

- #6 : 더한 Day에서 나머지로 요일 판별

'''