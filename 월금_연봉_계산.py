def yearly_payment(monthly_payment):
    before_tax = monthly_payment*12
    if before_tax <= 1200:
        tax = 0.06
    elif before_tax <= 4600:
        tax = 0.15
    elif before_tax <= 8800:
        tax = 0.24
    elif before_tax <= 1500:
        tax = 0.35
    elif before_tax <= 3000:
        tax = 0.38
    elif before_tax <= 5000:
        tax = 0.40
    else:
        tax = 0.42
    return (int(before_tax*(1-tax)))

monthly_payment = int(input("월급을 입력하세요: "))
yearly_pay = yearly_payment(monthly_payment)
print(f"세전 연봉: {monthly_payment*12}만원")
print(f"세후 연봉: {yearly_pay}만원")
