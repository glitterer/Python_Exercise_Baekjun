def find_even_number(n, m):
    numbers = [i for i in range(n, m + 1)]  # [1,2,3,4,5,6,7,8,9,10,11]
    if (n + m) % 2 == 0:
        middle = int((n + m) / 2 - 1)
        median = numbers[middle]
        for i in range(n, m + 1):
            if i % 2 == 0:
                print(f"{i} 짝수")
            if i == median:
                print(f"{i} 중앙값")
    else:
        for i in range(n, m + 1):
            if i % 2 == 0:
                print(f"{i} 짝수")

# 입력
while True:
    n = int(input("첫 번째 수 입력 : "))
    m = int(input("두 번째 수 입력 : "))
    if n < m:
        break
    elif n > m:
        print("첫 번째 수가 두 번째 수보다 큽니다. 다시 입력해주세요.")
        continue
    else:
        print("첫 번째 수와 두 번째 수가 같은 값입니다. 다시 입력해주세요.")

find_even_number(n, m)
