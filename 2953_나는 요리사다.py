contestant = []
cont_sum = []
for a in range(5):
    contestant.append(list(map(int, input().split())))
    cont_sum.append(sum(contestant[a]))
print(cont_sum.index(max(cont_sum))+1, max(cont_sum))
