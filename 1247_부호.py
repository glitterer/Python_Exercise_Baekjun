import sys
 
for _ in range(3):
    N = int(sys.stdin.readline())
    sum = 0
    for i in range(N):
       num = int(sys.stdin.readline())
       sum = sum + num 
    
    if sum > 0:
        print("+")
    elif sum < 0:
        print("-")
    else:
        print("0")
