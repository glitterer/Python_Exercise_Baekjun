a,b,v = map(int,input().split())
day = 1
height = 0
while True:
	height += a
	if height >= v:
		break
	else:
		height = height - b
		day += 1
print(day)

'''

a,b,v=map(int,input().split())

if (v-b)%(a-b)==0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)
'''
