# 📌Q1. 역사 문제를 하나 내보겠습니다.
# 고려시대와 조선시대 왕 이름 중에서 고려에도 있고 조선에도 있는 이름은 몇개 일까요? 한 번에 딱 안 떠오른다면 왕 이름을 드릴테니 파이썬 함수로 만들어서 출력 해봅시다.
# 조건1 - 중복되는 왕 이름 출력
# 조건2 - 중복되는 왕 이름의 수 출력

def king(korea_king, chosun_king):
    king_list = list()  # 왕 이름을 담을 dict

    korea = korea_king.split(",")  # 문자열을 ,기준으로 list로 변경
    chosun = chosun_king.split(",")  # 문자열을 ,기준으로 list로 변경

    for k in korea:
        if k in chosun:
            king_list.append(k)
            if king_list.count(k) == 1:
                print(f"조선과 고려에 모두 있는 왕 이름: {k}")
    print(f"조선과 고려에 모두 있는 왕 이름은 총 {len(set(king_list))}개 입니다.")


# 왕이름
korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"
king(korea_king, chosun_king)
