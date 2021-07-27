lists = [0]*4
for i in range(3):
    lists = list(map(int, input().split()))
    if lists.count(0) == 1:
        print('A')
    elif lists.count(0) == 2:
        print('B')
    elif lists.count(0) == 3:
        print('C')
    elif lists.count(0) == 4:
        print('D')
    elif lists.count(0) == 0:
        print('E')
