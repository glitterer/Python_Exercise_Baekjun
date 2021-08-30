count = 0
for i in range(1,9):
    n = input()
    if i % 2 == 1: 
        for k in range(0,7,2):
            if n[k] == 'F':
                count += 1
    else:
        for k in range(1,8,2):
            if n[k] == 'F':
                count += 1
print(count)
