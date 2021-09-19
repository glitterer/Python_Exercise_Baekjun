import sys
N = int(sys.stdin.readline())
N_arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_arr = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    if M_arr[i] in N_arr:
        print(1)
    else:
        print(0)
