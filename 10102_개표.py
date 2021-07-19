V = int(input())  #심사위원의 수
who = list(input())  #각 심사위원이 누구에게 투표했는지
# print(who)
cnt_A = 0
cnt_B = 0
for i in range(V):
    if who[i] == 'A':
        cnt_A = cnt_A + 1
    elif who[i] == 'B':
        cnt_B = cnt_B + 1
    else:
        continue
# print('A', cnt_A)
# print('B', cnt_B)
if cnt_A == cnt_B:
    print("Tie")
elif cnt_A > cnt_B:
    print('A')
else:
    print('B')
