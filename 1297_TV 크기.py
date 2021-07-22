diagnol, height, width = map(int, input().split())

res = diagnol / (height**2 + width**2)**0.5
print(int(height*res), int(width*res))
