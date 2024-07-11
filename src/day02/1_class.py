'''

'''
class Board :
    def __init__(self , num , content , date , writer ):
        self.num = num
        self.content = content
        self.date = date
        self.writer = writer

print( Board( 1 , '안녕하세요' , '2024-07-10' , '유재석') )
print( Board( 2 , '하하하하하' , '2024-07-11' , '강호동') )

class Member :
    def __init__(self , num , id , password , name ):
        self.num = num
        self.id = id
        self.password = password
        self.name = name

print( Member( 1 , 'qweqwe' , '1234' , '유재석') )
print( Member( 2 , 'asdasd' , '4567' , '강호동') )

class Product :

    # [4]번 할때 작성
    store = 'CU'

    def __init__(self , code , name , price , date ):
        self.code = code
        self.name = name
        self.price = price
        self.date = date

    # [2]번 할때 작성( 매개변수가 없고 리턴도 없는 메소드 )
    def info(self):
        print( f'store : { self.store } code : { self.code } name : { self.code } price : { self.price} date : { self.price }')

    # [3]번 할때 작성 ( 매개변수가 있고 리턴이 없는 메소드
    def priceUp(self  , increase  ):
        self.price += increase # self : 해당 메소드 를 호출한 객체의 속성
    #[3]번 할때 작성 ( 매개변수가 있고 리턴이 있는 메소드
    def priceDown(self , reduction ):
        self.price -= reduction
        return self.price
    #[3]
    def getPrice(self):
        return self.price

p1 = Product( 1 , '사과' , 3000 , '2024-07-10')
p2 = Product( 2 , '딸기' , 4000 , '2024-07-11')
print( p1 )
print( p2 )

# =========================================================== #
# [1] 객체의 속성 호출하기
# .(도트연산자)를 이용한 객체내 속성명 입력시 속성 값을 호출 합니다.
p3 = Product( 3 , '바나나' , 5000 , '2024-07-12')
print( p3 )
print( p3.code )
print( p3.name )
print( p3.price )
print( p3.date )
print( f' code : { p3.code } name : { p3.name } price : { p3.price} date : { p3.price }')
print( f' code : { p1.code } name : { p1.name } price : { p1.price} date : { p1.price }')
print( f' code : { p2.code } name : { p2.name } price : { p2.price} date : { p2.price }')

# [2] 객체의 메소드 사용하기
p3.info()
p1.info()
p2.info()

# [3] 메소드의 매개변수로 속성값 변경하기
# priceUp() : 클래스 안에 있는 메소드는 반드시 객체를 통해 사용합니다.
p3.priceUp( 2000 )
p3.info()

p3.priceDown( 1500 )
p3.info()

price = p3.getPrice()
print( price )


# [4]
p3.store = 'GS'
p3.info()







