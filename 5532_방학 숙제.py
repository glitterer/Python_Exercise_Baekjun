days = int(input())
korean =  int(input())
maths =  int(input())
maxKorean =  int(input())
maxMaths =  int(input())
if korean%maxKorean != 0:
    koreanDays = korean // maxKorean + 1
else:
    koreanDays = korean // maxKorean
if maths % maxMaths != 0:
    mathsDays = maths // maxMaths + 1
else:
    mathsDays = maths // maxMaths
maxDays = max(koreanDays, mathsDays)
print(days - maxDays)
