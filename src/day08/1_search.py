# https://github.com/itdanja/week_python_202208/tree/master/7%EC%9D%BC%EC%B0%A8


'''
    검색[탐색] : 정렬이 있는 상태 vs 정렬 없는 상태
        1. 순차 검색 : 순서대로 저장되어 있는 자료를 처음부터 끝까지 순서대로 검색
            1. 정렬 없는 상태      2.속도 많이 느림     3.반복문 이용한 구현

        2. 이진(이분) 검색 : 가운데에 있는 항목을 비교해서 작으면 왼쪽 , 크면 오른쪽 검색
            1. 정렬 되어있는 상태   2.퀵 정렬 유사[ 순차검색 보다는 효율성 좋다 ]

        3. 이진 트리 검색 : 이진트리(4일차)를 이용한 검색 방법
        4. 해싱 검색 : 키가 있는 위치를 계산하여 바로 찾아가는 검색 방식( 딕셔너리 )

'''
"""
    순차검색 : 정렬이 안되어 있는 상태에서 검색[찾기/탐색]
"""
# 순차검색 구현 [ for문 이용한 ] : 중복검색 불가능
def seqSearch( ary , fdata ) :  # 인수 : 배열 , 검색할데이터
    pos = -1                                # 검색 성공시 의 찾은 인덱스 위치를 저장할 변수 [ -1 : 인덱스 없다 -> 검색X ]
    size = len( ary )                   # 배열의 길이
    for i in range( size ) :        # 배열의 길이만큼 반복
        if ary[i] == fdata :          # 만약에 i번째 인덱스의 데이터가 검색할 데이터와 같으면
            pos = i                         # 해당 인덱스를 pos 변수에 저장
            break                       # 찾았으면 반복문 종료
    return pos                      # 함수 종료시 찾은 pos변수를 반환

# 임의의 배열[리스트]
dataAry = [ 120 , 188 , 150 , 168 , 162 , 105 , 120 , 177 , 50 ]
# 검색 데이터 입력
finddata =  int( input("검색할 데이터: ") )
pos =  seqSearch( dataAry , finddata )
if pos == -1 : # 만약에 -1 이면 인덱스 없다
    print( finddata , '가 없습니다. ')
else :
    print( finddata , '는 ' , pos , '위치에 있음 ')



"""
    순차검색[ 중복 검색이 가능한 ]
"""
def seqSearch( ary , fdata ) :
    poslist = [ ]   # 검색된 인덱스를 여러개 저장하기 위한 배열 선언
    size = len( ary )
    for i in range( size ) :
        if ary[i] == fdata :
            # 만약에 i번째 인덱스의 데이터가 검색할데이터 와 같으면
            # poslist에 찾은 데이터의 인덱스 저장
            poslist.append( i )
    return poslist # 함수 종료시 poslist 반환

# 임의의 배열[ 중복값이 존재하는 리스트]
dataAry = [ 120 , 188 , 150 , 168 , 162 , 105 , 120 , 177 , 50 ]
# 검색 데이터 입력받기
finddata = int( input('검색할 데이터 : ') )
poslist = seqSearch( dataAry , finddata )
if poslist == [ ] : # 만약에 postlist 배열이 비어 있으면
    print( finddata,'가 없습니다.')
else :
    print( finddata,'는 ', poslist, '위치에 있음')


"""
    순차검색 [ 정렬이 되어 있는 상태 ]
"""
def seqSearch( ary , fdata ) :
    postlist = [ ]
    for i in range( len(ary) ) :
        if ary[i] == fdata :
            #만약에 i번째 인덱스의 데이터가 검색데이터와 같으면
            postlist.append( i ) # 배열[리스트] 추가
        elif ary[i] > fdata :   # 만약에 i번째 인덱스의 데이터가 검색데이터보다 크면
            break # 검색종료
            # [ 정렬이 되어 있는상태에서 검색데이터가 i번째 데이터보다 작으면   ]
    return postlist

# 임의의 배열
dataAry = [ 120 , 188 , 150 , 168 , 162 , 105 , 120 , 177 , 50 ]
# 검색 입력받기
fdata = int( input('검색 데이터 : ') )
# 정렬[ 파이썬에서 제공하는 정렬 함수 사용 ]
dataAry.sort( )      # 오름차순

poslist = seqSearch( dataAry , fdata )
if poslist == [] :
    print( fdata , '가 없습니다. ')
else:
    print( fdata ,'는 ' ,poslist,'위치에 있습니다. ')

'''
    50 50 50 105 120 168 177 188
    검색 : 120
        50 == 120
        50 == 120
        50 == 120
        105 == 120
        120 == 120  [ 찾음 ] 
        168 == 120  ~~~~~~~~~ 불필요한 코드 
        177 == 120
        188 == 120
'''