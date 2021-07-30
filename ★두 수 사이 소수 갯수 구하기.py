def count_prime_number(n, m):
    cnt = 0
    for i in range(n, m+1):  # n과 m사이에 있는 숫자들 ==> n과 m을 포함한다.
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
        if flag != 1:
            cnt += 1
    if n == 1:
        print("소수개수", cnt-1)
    else:
        print("소수개수", cnt)


# 입력
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
count_prime_number(n, m)
