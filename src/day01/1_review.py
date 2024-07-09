''' [python1] 구현
        1. 상품의 가격 과 등급을 입력받아 처리하는 함수 만드시오.
        2. 상품 가격 등급 표
            price   grade
            2500    'V'
            96900   'S'
            124000  'G'
        3. 입력받은 가격과 등급을 함수의 매개변수로 전달하여 해당 구매 여부 판단후 잔돈 출력 하시오.
            만약에 존재 하지 않는 등급이면 '존재 하지 않는 등급 입니다.' 출력 하시오.
            만약에 금액이 부족 하면 '금액이 부족 합니다' 출력 하시오.
            매개변수의 등급도 일치하고 매개변수의 가격도 부족하지 않으면 잔돈 출력하시오.
            EX)  3000  , 'V'    --->  500
            EX)  90000 , 'S'    --->  '금액이 부족 합니다'
            EX)  90000 , 'C'    --->  '존재 하지 않는 등급 입니다.'
'''
# [1] 함수 정의
def method1( price , grade ) :
    if grade == 'V' :
        if price >= 2500 :
            return f'잔돈 : {price - 2500}'
    elif grade == 'S' :
        if price >= 96900 :
            return f'잔돈 : {price - 96900}'
    elif grade == 'G' :
        if price >= 124000 :
            return f'잔돈 : {price - 124000}'
    else :
        return '존재 하지 않는 등급 입니다.'
    # 등급은 동일하지만 금액이 충족하지 않을때 RETURN 못나서 아래 리턴을 만나게 된다.
    return '금액이 부족 합니다.'
# [2] 함수 호출
while True :
    price = int( input('[price] : ') )
    grade = input( '[grade] : ' )
    result = method1( price , grade )
    print( result )










