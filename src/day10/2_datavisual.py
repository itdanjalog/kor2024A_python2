
import matplotlib.pyplot as plt

# 데이터 생성 (0부터 10까지의 값)
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0, 0.5, 1, 0.5, 0, -0.5, -1, -0.5, 0, 0.5, 1]  # y = sin(x)와 비슷한 형태로 임의 데이터 생성

# 선 그래프 그리기
# 선 차트(Line Chart)는 시간에 따른 데이터의 변화를 시각적으로 나타내는 그래프입니다. 데이터 포인트를 선으로 연결하여, 연속적인 데이터의 경향성을 쉽게 파악할 수 있습니다.
plt.plot(x, y, label='y data', color='blue', linewidth=2, marker='o')
plt.title('Line chart ')
plt.xlabel('X-axios')
plt.ylabel('Y-axios')
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.5, linestyle='--')
plt.grid()
plt.legend()
plt.show()

# 데이터 생성
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 5, 2, 8]

# 막대 그래프 그리기
# 막대차트(Bar Chart)는 데이터를 직사각형의 막대로 나타내는 그래프입니다. 각 막대의 길이는 해당 데이터의 값을 나타내며, 막대의 높이나 길이를 통해 여러 범주 간의 비교를 쉽게 할 수 있습니다.
plt.bar(categories, values, color='orange')
plt.title('Bar chart ')
plt.xlabel('X-axios')
plt.ylabel('Y-axios')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 데이터 생성
import random
x = [  random.random(  ) for _ in range( 50 ) ]  # 0과 1 사이의 50개 랜덤 수
y = [  random.random(  ) for _ in range( 50 ) ]  # 0과 1 사이의 50개 랜덤 수
sizes = 50

# 산점도 그리기
#산점도(Scatter Plot)는 두 개의 변수 간의 관계를 시각적으로 나타내는 그래프입니다. 각각의 데이터 포인트는 두 변수의 값을 x축과 y축에 대응시켜 점으로 표시됩니다. 산점도를 통해 변수 간의 상관관계, 분포, 경향성을 쉽게 파악할 수 있습니다.
plt.figure(figsize=(10, 5))
plt.scatter(x, y, s=sizes, alpha=0.5, c='green', edgecolors='w')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid()
plt.show()

'''
    plt.plot(x, y, label='y data', color='blue', linewidth=2, marker='o'):
    
    x와 y 데이터를 사용하여 선 그래프를 그립니다.
    label='y data': 그래프의 범례에 사용할 레이블을 지정합니다.
    color='blue': 선의 색상을 파란색으로 설정합니다.
    linewidth=2: 선의 두께를 2로 설정합니다.
    marker='o': 데이터 포인트에 원형 마커를 추가합니다.
    plt.title('Line chart '):
    
    그래프의 제목을 'Line chart'로 설정합니다.
    plt.xlabel('X-axios'):
    
    x축의 레이블을 'X-axios'로 설정합니다.
    plt.ylabel('Y-axios'):
    
    y축의 레이블을 'Y-axios'로 설정합니다.
    plt.axhline(0, color='gray', linewidth=0.5, linestyle='--'):
    
    y=0인 수평선을 그립니다.
    color='gray': 선의 색상을 회색으로 설정합니다.
    linewidth=0.5: 선의 두께를 0.5로 설정합니다.
    linestyle='--': 선의 스타일을 점선으로 설정합니다.
    plt.axvline(0, color='gray', linewidth=0.5, linestyle='--'):
    
    x=0인 수직선을 그립니다.
    위와 같은 스타일 옵션이 적용됩니다.
    plt.grid():
    
    그래프에 그리드를 추가하여 읽기 쉽게 만듭니다.
    plt.legend():
    
    그래프의 범례를 추가합니다. 이 경우에는 label='y data'로 설정된 범례가 추가됩니다.
    plt.show():
    
    그래프를 화면에 표시합니다.
    
    --- 
    이 코드를 실행하면 주어진 x와 y 데이터를 기반으로 한 선 그래프가 나타나며, 제목, 축 레이블, 그리드, 수직 및 수평선, 그리고 범례가 포함됩니다.
    
    ###########################################################################################
    plt.bar(categories, values, color='orange'):

    categories는 막대 그래프의 각 막대를 나타내는 카테고리(예: 이름, 날짜 등)입니다.
    values는 각 카테고리에 대한 값(예: 수치, 빈도수 등)입니다.
    color='orange': 막대의 색상을 주황색으로 설정합니다.
    plt.title('Bar chart '):
    
    그래프의 제목을 'Bar chart'로 설정합니다.
    plt.xlabel('X-axios'):
    
    x축의 레이블을 'X-axios'로 설정합니다. (축 레이블에 맞는 실제 명칭으로 수정하는 것이 좋습니다.)
    plt.ylabel('Y-axios'):
    
    y축의 레이블을 'Y-axios'로 설정합니다. (역시 적절한 명칭으로 수정하는 것이 좋습니다.)
    plt.grid(axis='y', linestyle='--', alpha=0.7):
    
    y축 방향에만 그리드를 추가합니다.
    linestyle='--': 그리드 선의 스타일을 점선으로 설정합니다.
    alpha=0.7: 그리드의 투명도를 0.7로 설정하여 조금 더 부드럽게 보이도록 합니다.
    plt.show():
    
    그래프를 화면에 표시합니다.
    
    --
    이 코드를 실행하면 주어진 categories와 values 데이터를 기반으로 한 막대 그래프가 나타나며, 제목, 축 레이블, y축에 대한 그리드가 포함됩니다. 막대의 색상은 주황색으로 설정되어 있습니다.
    
    ###########################################################################################
    plt.figure(figsize=(10, 5)):

    새로운 Figure 객체를 생성하며, 그래프의 크기를 가로 10인치, 세로 5인치로 설정합니다.
    plt.scatter(x, y, s=sizes, alpha=0.5, c='green', edgecolors='w'):
    
    x와 y는 산점도의 데이터 포인트의 좌표입니다.
    s=sizes: 각 포인트의 크기를 sizes 배열에 지정된 값에 따라 설정합니다.
    alpha=0.5: 포인트의 투명도를 0.5로 설정하여 반투명하게 만듭니다.
    c='green': 포인트의 색상을 녹색으로 설정합니다.
    edgecolors='w': 포인트의 외곽선 색상을 흰색으로 설정합니다.
    plt.title('Scatter Plot Example'):
    
    그래프의 제목을 'Scatter Plot Example'로 설정합니다.
    plt.xlabel('X-axis'):
    
    x축의 레이블을 'X-axis'로 설정합니다.
    plt.ylabel('Y-axis'):
    
    y축의 레이블을 'Y-axis'로 설정합니다.
    plt.xlim(0, 1):
    
    x축의 범위를 0에서 1로 설정합니다. 이 범위 내에서 x값이 표시됩니다.
    plt.ylim(0, 1):
    
    y축의 범위를 0에서 1로 설정합니다. 이 범위 내에서 y값이 표시됩니다.
    plt.grid():
    
    그래프에 그리드를 추가하여 포인트의 위치를 쉽게 파악할 수 있도록 합니다.
    plt.show():
    
    그래프를 화면에 표시합니다.
    
    --
    이 코드를 실행하면 주어진 x와 y 데이터에 따라 산점도가 나타나며, 각 포인트는 sizes에 따라 크기가 다르고, 녹색으로 표시되며, 외곽선은 흰색입니다. 그래프의 제목과 축 레이블, 그리드가 포함되어 있으며, x축과 y축의 범위가 각각 0에서 1로 설정되어 있습니다.

'''