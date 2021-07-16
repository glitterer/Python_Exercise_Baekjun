import sys
repeat = int(input())
for i in range(0, repeat):
    num = int(sys.stdin.readline())  # sys를 반드시 사용해야 시간초과가 발생하지 않는다.
    print(int(num)**2)


'''
repeat = int(input())
for i in range(0, repeat):
    num = int(input())
    print(num**2)
'''
