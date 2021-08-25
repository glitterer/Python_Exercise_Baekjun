num = int(input())
member_list = []
for _ in range(num):
    age, name = map(str, input().split())
    age = int(age)
    member_list.append((age, name))
# print(member_list)
# 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서
member_list.sort(key = lambda x: x[0])
# print(member_list)
for i in member_list:
    print(i[0], i[1])
