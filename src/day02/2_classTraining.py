accountBook = [ ]
staticNum = 0
class Account :
    def __init__(self , num , item , amount , date ):
        self.num = num
        self.item = item
        self.amount = amount
        self.date = date

    def create(self):
        accountBook.append( self )
        print('등록 되었습니다.')
    def read(self):
        print( f'{self.num:<10}{self.item:<10}{self.amount:<10}{self.date:<10}')
    def delete(self):
        accountBook.remove( self )
        print('삭제 되었습니다.')

while True :
    ch = int( input('1.등록 2.출력 3.삭제 : '))
    if ch == 1 :
        staticNum+=1
        item =  input('항목명:')
        amount = int( input('금액:'))
        date = input('날짜:')
        account = Account( staticNum , item , amount , date )
        account.create()
    elif ch == 2 :
        print( f'{'순번':<10}{'항목':<10}{'금액':<10}{'날짜':<10}')
        for account in accountBook :
            account.read()
    elif ch == 3 :
        deleteNum = int( input('삭제할 순번 : ') )
        for account in accountBook :
            if account.num == deleteNum :
                account.delete()
                break




