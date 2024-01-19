import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 사용하는 운영체제의 한글 폰트 경로로 변경
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

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
