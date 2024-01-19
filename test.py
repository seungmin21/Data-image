import matplotlib.pyplot as plt

# 데이터 생성
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 선 그래프 그리기
plt.plot(x, y)

# 제목과 레이블 추가
plt.title('간단한 선 그래프')
plt.xlabel('X 축')
plt.ylabel('Y 축')

# 그래프 표시
plt.show()
