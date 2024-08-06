'''
파이썬에서 시각화는 데이터 분석의 중요한 부분으로, 데이터를 그래프나 차트 형태로 표현하여 패턴이나 인사이트를 쉽게 파악할 수 있도록 돕습니다.
주요 시각화 라이브러리로는 Matplotlib, Seaborn, Pandas, Plotly, Bokeh 등이 있습니다. 각 라이브러리의 특징과 간단한 예제를 소개할게요.
'''


import matplotlib.pyplot as plt

plt.title("chart1")
plt.plot([1, 4, 9, 16])
plt.show()

plt.title("chart2")
plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
plt.show()


plt.title('chart3')
plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
plt.xlabel(" x-axios label")
plt.ylabel( 'y-axios label')
plt.show()

# 데이터 생성
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 선 그래프 그리기
plt.title("chart4")
plt.plot(x, y )
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.grid()
plt.show()


