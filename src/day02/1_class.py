'''

    객체      : 클래스에서 (속성,함수)정의 된 토대로 메모리 공간 할당
    클래스    : 객체를 생성하기 위한 (속성,함수)를 정의하는 일종의 틀/설계도
    클래스 만드는/정의하는 방법
        - 클래스명 : 관례적으로 클래스명은 첫글자를 대문자로 하기
        - 클래스의 (구성)멤버
            - def __init__(self , 매개변수1 , 매개변수2 , 매개변수3 ):      객체 생성시 객체의 속성의 초기(처음) 값 을 대입 할때 사용
                self.속성명 = 매개변수1
                self.속성명 = 매개변수2
                self.속성명 = 매개변수3

            - self : 현재 생성 되는 객체를 뜻
            - 매개변수명 과 self.속성명 은 관례적 동일하게 작성하는 경우가 많다. ( 해당 매개변수의 값이 어디에 대입 될지 구분하기 쉽게 하기 위해 )
            - 속성 : 객체가 가지는 고유한 특성의 값

        class 클래스명 :
            def __init__(self , 매개변수1 , 매개변수2 , 매개변수3 ) :
                self.속성명 = 매개변수1
                self.속성명 = 매개변수2
                self.속성명 = 매개변수3

    정의된 클래스 를 이용한 객체 생성 하는 방법
        [1] 클래스명( 속성초기값 , 속성초기값 , 속성초기값 )
        [2] 변수명 = 클래스명( 속성초기값 , 속성초기값 , 속성초기값 )
            - 변수 가 필요한 이유 : 해당 객체를 변수에 저장한 후 추후에 반복적으로 객체를 사용하기 위해서는 변수가 필요하다.

'''
# 예)
# [1] 특정 프로그램의 방문록 들을 관리하는 메모리 설계
    # (게시물이 가질수 있는 속성/특성 ) 방문록번호,방문록내용,방문록작성일,방문록작성자 여러개 관리하는 클래스 설계
class Board :
    def __init__( self , 번호 , 내용 , 작성일 , 작성자 ):
        self.num = 번호
        self.content = 내용
        self.date = 작성일
        self.writer = 작성자
# 객체 생성
print(  Board( 1 , '안녕하세요' , '2024-07-11' , '유재석')  )
b1 = Board( 2 , '안녕하세요2' , '2024-07-12' , '강호동' )
print( b1 )

# [2] 특정 프로그램의 회원 들을 관리하는 메모리 설계
    # 회원번호 , 아이디 , 비밀번호  , 회원명 들을 가지는 속성을 여러개 관리하는 클래스 설계
class Member :
    def __init__(self , num , id , password , name ):
        self.num = num
        self.id = id
        self.password = password
        self.name = name
# 객체 생성
m1 = Member( 1 , "qweqwe" , "1234" , "유재석" )
m2 = Member( 2 , "asdasd" , "4567" , "강호동" )    # <__main__.Member object at 0x000001F67E4D83E0> 객체가 저장된 메모리의 위치번호
print( m1 )
print( m2 )

# [3] 특정 프로그램의 제품 들을 관리하는 메모리 설계
    # 제품코드 , 제품명 , 가격 , 등록일 들을 가지는 속성을 여러개 관리하는 클래스 설계
class Product :
    def __init__(self , code , name , price , date ):
        self.code = code
        self.name = name
        self.price = price
        self.date = date
# 객체 생성
p1 = Product(  1, '사과' , 3000 , '2024-07-11' )
p2 = Product(  2 , '바나나' , 5000 , '2024-07-12' )
print( p1 )
print( p2 )

# [ 실습 ] 자동차 들을 관리하는 메모리 설계
    # 색상 , 속도 , 제조사 , 차량 번호 들을 가지는 속성을 여러개 관리하는 클래스 설계
    # 임의 의 값으로 객체 2개 생성
class Car : # 추상적으로 생각한 (속성,함수)를 가지는 객체의 클래스를 설계
    def __init__(self , color , speed , manufacturer , carNumber):
        self.color = color      # 색상
        self.speed = speed      # 속도
        self.manufacturer = manufacturer    #제조사
        self.carNumber = carNumber  #차량번호
# 객체 생성 ( 클래스가 준비물 )
내차 = Car( '노랑' , 0 , '현대' , '1234' ) # 차 1대 생성
친구차 = Car( '빨강' , 0 , '기아' , '4567' ) # 차 1대 생성
    # **클래스/설계도 는 같지만 서로 다른 객체( 서로 다른 메모리 )가 만들어 진다.!!!!!!!!
print( 내차 )      # 0x000001CFD1E2F1A0
print( 친구차 )    # 0x000001CFD1E2F1D0


































