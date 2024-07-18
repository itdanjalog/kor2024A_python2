
# 파이썬 => 데이터 가공/다루기 =>
# CSV 파일 다루기

import csv  # csv 관련된 함수 제공

# 1. csv 파일 가져오기
file = open("file1.csv", "r" ) # 해당 파일 읽기 모드[r]
# 2. csv 파일 읽기
rows = csv.reader(file) # csv.reader(파일객체) : 해당 파일의 내용을 줄당 1하나의리스트 => 2차원리스트 로 읽기
print( type( rows ))

# 3. csv 출력
for row in rows :
    print( row )
    for col in row :
        print( col )

# 4. csv 파일 쓰기
file = open("file2.csv", "w" , newline="" ) # 해당 파일 쓰기 모드[w]
contents = csv.writer( file , delimiter =','  )   # 쓰기설정 [ delimiter : 요소들의 구분 기준 ]

content = [ ["유재석","강호동","신동엽"] , [90,80,70] , [60,80,70] ]
contents.writerows( content ) # 쓰기
####################################################################