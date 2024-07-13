'''
    객체형 가계부 만들기
        1. 아래 속성과 함수 기준으로 클래스 설계
            - 객체의 속성 : 번호 , 항목명 , 금액 , 날짜
            - 객체의 함수 : 등록() , 출력() , 삭제()
        2. 함수 구현
            - 번호는 입력 받지 않고 자동 으로 1부터 증가 하면서 등록 될수 있도록 한다.
            등록(create)  : 항목명 , 금액 , 날짜를 입력받아 객체 생성 하고 생성된 객체를 리스트(accountBook) 저장 하시오.
            출력(read)    : 현재 객체의 속성들의 값 출력 하시오.
            삭제(delete)  : 현재 객체를 리스트에서 제거 하시오.
'''
accountBook = [ ] # 여러 개의 Account 객체를 저장 하는 리스트 선언
class Account :  # Account 클래스 정의/만들기
    def __init__(self , 번호 , 항목명 , 금액 , 날짜 ): # 객체의 속성 초기화
        # self.num            # self.num : 해당 클래스의 속성명 정의
        self.num = 번호       # self.num = 번호   : 정의된 속성명(num) 에 매개변수(번호) 값 대입
        self.item = 항목명     # self.item = 항목명   : 정의된 속성명(item) 에 매개변수(항목명) 값 대입
        self.money = 금액     # self.money = 금액   : 정의된 속성명(money) 에 매개변수(금액) 값 대입
        self.date = 날짜      # self.date = 날짜   : 정의된 속성명(date) 에 매개변수(날짜) 값 대입
    # 함수
    # 1. 객체를 리스트에 저장
    def create( self ): # self : 해당 함수를 호출하는 객체 뜻
        print('>> list create')
        accountBook.append( self ) # 리스트에 요소 저장 :  .append( 객체 ) , 리스트에 해당 객체를 저장
        # unlocal(함수밖,클래스밖) 변수는 함수내부 또는 클래스내부 에서 호출이 가능

    # 2. 객체의 모든 속성의 값 호출
    def read( self ):
        print( f'{self.num:<10}{self.item:<10}{self.money:<10}{self.date:<10}')

    # 3. 객체를 리스트에서 삭제
    def delete( self ):
        print('>> list delete')
        accountBook.remove( self ) # 리스트에 요소 삭제 :  .remove( 객체 ) , 리스트에 해당 객체를 삭제


staticNum = 1 # 등록시 1부터 1씩 증가 하는 번호를 가지고 있는 변수
while True :
    ch = int( input('1.create 2.read 3.delete ') )
    if ch == 1 :
        # 입력받기
        item = input('항목명 : ')
        money = int( input('금액 : ') )
        date = input('날짜 : ')
        # 4개의 변수를 하나의 객체로 만들고 생성된 객체 주소 값을 변수에 대입
        account = Account( staticNum , item , money , date )
        # 생성된 객체를 리스트 에 저장
        account.create()
        # 등록 번호를 증가
        staticNum += 1

    elif ch == 2 :
        print( f'{'순번':<10}{'항목명':<10}{'금액':<10}{'날짜':<10}')
        # 리스트내 모든 요소(객체)를 출력
        for account in accountBook :
        # accountBook : account 객체 들이 저장된 리스트
        # account : 리스트내 저장된 각 account 객체들
            account.read()  # 해당 요소의 account객체의 출력 메소드 호출

    elif ch == 3 :
        # 삭제할 순번을 입력받기
        deleteNum = int( input('삭제할 항목 번호 : ') )
        # 입력받은 순번을 리스트내 객체 '순번'속성에서 동일한 값 찾기
        for account in accountBook :
            # 리스트내 요소(객체)를 하나씩 순회하면서 객체 꺼내기
            if account.num == deleteNum :
                # 해당 객체내 순번이 입력받은 삭제할 순번과 같으면
                account.delete()
                # 해당 객체의 삭제 함수 호출
                break
                # 삭제를 1개만 할 예정 이라서 삭제가 되었으면 break 이용한 for반복문 종료
























