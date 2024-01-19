import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn 스타일 설정
sns.set(style="whitegrid")

# 예제 데이터 로드
tips = sns.load_dataset("tips")

# 히스토그램 그리기
sns.histplot(tips['total_bill'], kde=True)

# 그래프 표시
plt.show()