import sys
exist = []
cnt = 0
for i in range(8):
    exist.append(sys.stdin.readline())
    if i % 2 == 0:
        j = 0
        for j in range(8):
            if j % 2 == 0:
                if exist[i][j] == 'F':
                    cnt += 1
                    j += 1
    else:
        j = 0
        for j in range(8):
            if j % 2 == 1:
                if exist[i][j] == 'F':
                    cnt += 1
                    j += 1
print(cnt)
