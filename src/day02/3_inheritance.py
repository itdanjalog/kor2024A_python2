'''
    클래스에서 상속이란, 물려주는 클래스(Parent Class, Super class)의 내용(속성과 메소드)을 물려받는 클래스(Child class, sub class)가 가지게 되는 것입니다.
    예를 들면 국가라는 클래스가 있고, 그것을 상속받은 한국, 일본, 중국, 미국 등의 클래스를 만들 수 있으며, 국가라는 클래스의 기본적인 속성으로 인구라는 속성을 만들었다면, 상속 받은 한국, 일본, 중국 등등의 클래스에서 부모 클래스의 속성과 메소드를 사용할 수 있음을 말합니다.
    기본적인 사용방법은 아래와 같습니다.
    자식클래스를 선언할때 소괄호로 부모클래스를 포함시킵니다.
    그러면 자식클래스에서는 부모클래스의 속성과 메소드는 기재하지 않아도 포함이 됩니다.
'''
class Korea:
    """Super Class"""
    countryName = '대한민국'
    population = '5163'
    capital = '서울'

    def show(self):
        print('Korea 클래스의 메소드입니다.')


class Person(Korea):
    """Sub Class"""
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print('Person 클래스의 메소드입니다.')

a = Person('유재석')
a.show()
a.show_name()
print( a.name )
print( a.capital )
print( a.countryName )

a = Person('강호동')
a.show()
a.show_name()
print( a.name )
print( a.capital )
print( a.countryName )
