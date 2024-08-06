import csv
# (1) 해당 파일을 open해서 파일객체로 가져오기
csvFile = open( 'data_0124_20240806.csv' , 'r' )
# (2) 해당 파일을 csv 함수( reader ) 이용한 파일 읽어오기
csvContent = csv.reader( csvFile )
# (3) 반복문을 이용한 행/줄 단위로 출력
날짜목록 = []
종가목록 = []
for row in list(csvContent)[1:20] :
    print( row[0] )
    날짜목록.append( f'{row[0].split('/')[1]}/{row[0].split('/')[2]}' )
    print( row[1] )
    종가목록.append( int( row[1] ) )
    # (4) 반복문을 이용한 현재 행/줄 단위의 열 단위 출력

import matplotlib.pyplot as plt

print( 종가목록 )

plt.title("x ticks")
plt.plot(날짜목록, 종가목록 )
plt.show()

날짜목록.reverse()
종가목록.reverse()
print( 종가목록 )

plt.title("x ticks")
plt.plot(날짜목록, 종가목록 )
plt.show()

