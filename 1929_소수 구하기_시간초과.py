# 시간초과 1
n, m = list(map(int, input().split()))
for i in range(n, m+1):  # n과 m사이에 있는 숫자들 ==> n과 m을 포함한다.
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
    if flag != 1:
        print(i)

'''
#시간초과 2

def count_prime_number(n, m):
    for i in range(n, m+1):  # n과 m사이에 있는 숫자들 ==> n과 m을 포함한다.
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
        if flag != 1:
            print(i)


# 입력
n, m = list(map(int, input().split()))
count_prime_number(n, m)
'''
