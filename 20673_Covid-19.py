p_avg_case = int(input())
q_avg_newHospital = int(input())

if p_avg_case <= 50 and q_avg_newHospital <= 10:
    print("White")
elif q_avg_newHospital > 30:
    print("Red")
else:
    print("Yellow")
