g1 = input()
g2 = input()
g3 = input()
g4 = input()
g5 = input()
g6 = input()
 
game = [g1, g2, g3, g4, g5, g6]
 
win = 0
lose = 0
 
for i in game:
    if i == "W":
        win += 1
    else:
        lose += 1
 
if win == 5 or win == 6:
    print(1)
elif win == 3 or win == 4:
    print(2)
elif win == 1 or win == 2:
    print(3)
else:
    print(-1)
