# 현재 첫 번째 줄만 잘 출력이 된다
# 두 번째 줄 출력을 어떻게 해야할지 도저히 감이 안 잡히는 상황이다...

def score(sang_rps, opponent_rps):
    total_score = 0
    cnt = 0
    for i in opponent_rps:
        if sang_rps[cnt] == 'S':
            if i == 'S':
                total_score += 1
            elif i == 'P':
                total_score += 2
            elif i == 'R':
                total_score += 0
        elif sang_rps[cnt] == 'P':
            if i == 'S':
                total_score += 0
            elif i == 'P':
                total_score += 1
            elif i == 'R':
                total_score += 2
        elif sang_rps[cnt] == 'R':
            if i == 'S':
                total_score += 2
            elif i == 'P':
                total_score += 0
            elif i == 'R':
                total_score += 1
        cnt += 1
    return total_score


# 라운드 수
rounds = int(input())
sang_rps = list(map(str, input()))  # 상근이가 각 라운드에 낸 모양 (S, P, R)
N = int(input())  # 훈련친구 N명
total_score = [0]*N
sang_score = 0
for i in range(N):
    opponent_rps = list(map(str, input()))  # 상대방의 각 라운드에 낸 모양 (S, P, R)
    total_score[i] = score(sang_rps, opponent_rps)
    sang_score += total_score[i]
print(sang_score)  # 상근이의 점수
