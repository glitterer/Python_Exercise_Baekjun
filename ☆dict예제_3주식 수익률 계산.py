# 📌Q3. 예금 금리가 너무 낮아서 주식을 시작했습니다.
# 아래와 같이 매수한 종목 이름, 수량, 매수 평균 금액이 있습니다.
# 판매가는 따로 주어집니다.
# 종목과 수익률만 출력하시고 종목별 수익률이 높은 순서대로 출력해주세요. (소수 둘째자리까지 출력)
# 수익률 = ((매도가 - 매수가) / 매수가) X 100


def stock_profit(stocks, sells):
    stocks = stocks.split(',')  # , 기준으로 분리
    stocks = [s.split("/") for s in stocks]  # / 기준으로 분리

    # 종목명, 수량, 매수평균금액, 종목별수익률을 저장할 dict 생성
    profit_dict = dict()
    profits = []  # 종목별수익률을 저장할 리스트

    # 수익률 계산
    for p in range(len(sells)):
        profits.append((sells[p] - int(stocks[p][2])) / int(stocks[p][2]) * 100)

    # dict로 만들어서 정렬
    index_cnt = 0
    for k in stocks:
        profit_dict[k[0]] = profits[index_cnt]
        index_cnt += 1
    profit_dict = sorted(profit_dict.items(), key=lambda x: x[1], reverse=True)  # lambda를 통해서 dict를 정렬하는 방법
    # print(profit_dict)

    for i in range(len(profit_dict)):
        print(f"{profit_dict[i][0]}의 수익률 {profit_dict[i][1]:.3}")


stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]
stock_profit(stocks, sells)
