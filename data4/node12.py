import pandas as pd 
from scipy import stats
import numpy as np

# 데이터 불러오기
user_data = pd.read_csv('C:/Users/USER/Downloads/data (1).csv')

# 데이터의 상위 5번째 행까지 출력
print(user_data.head())

# # Z-score 계산 
# z_scores = stats.zscore(user_data.iloc[:, 1:], axis=0)  

# # Z-score 절대값 계산
# z_scores = np.abs(z_scores)

# # Z-score 출력
# z_scores

# # 임계값(threshold) 설정
# threshold = 3

# # z-score 기준으로 이상치를 찾아서 outlier 컬럼에 이상치 여부 기입 (0: 정상, 1:이상치)
# user_data['outlier'] = (z_scores > threshold).any(axis=1).astype(int)
# print(user_data.head())

# # 시각화에 필요한 라이브러리 불러오기
import matplotlib.pyplot as plt 

# # user_data['outlier']을 활용하여 이상치 여부에 따른 확률 계산
# # value_counts()는 열의 고윳값의 개수를 반환하지만 normalize=True를 사용하면 열에 있는 값의 개수 비율(상대적 빈도)을 반환함
# outlier_percentage = pd.value_counts(user_data['outlier'], normalize=True) * 100

# # 시각화 자료 크기 조정
# plt.figure(figsize=(3, 4))

# # outlier_percentage라는 데이터로 bar chart 시각화
# # x축 값을 0과 1로 지정
# bars = plt.bar(['0', '1'], outlier_percentage)

# # 퍼센트(%) 표시
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, yval/2, f'{yval:.2f}%', fontsize=10, va='center', ha='center')

# plt.title('Normal(0) vs Outlier(1)') # 표 제목
# plt.yticks(ticks=np.arange(0, 101, 10)) # y축 표기 (0~100까지 10단위로 증가)
# plt.ylabel('Percentage (%)') # y축 범례
# plt.xlabel('Outlier') # x축 범례
# plt.show() # 출력

# # 정상 데이터만 필터링 
# user_data = user_data[user_data['outlier'] == 0] 

# # outlier 컬럼 삭제 
# user_data = user_data.drop(columns=['outlier'])

# # DataFrame의 인덱스를 리셋하고, 이전 인덱스를 컬럼으로 추가하지 않음
# user_data.reset_index(inplace=True, drop=True)
# user_data.head()

print("////////////////////////////////////////////////")

# 시각화 라이브러리 불러오기
import seaborn as sns  

# # 'CustomerID' 열을 제외(drop)하고 상관 관계 행렬 계산(corr())
# corr = user_data.drop(columns=['CustomerID']).corr()

# # 행렬이 대각선을 기준으로 대칭이기 때문에 하단만 표시하기 위한 마스크 생성
# mask = np.zeros_like(corr) # np.zeros_like()는 0으로 가득찬 array 생성, 크기는 corr와 동일   
# mask[np.triu_indices_from(mask, k=1)] = True # array의 대각선 영역과 그 윗 부분에 True가 들어가도록 설정

# # 히트맵 그리기
# plt.figure(figsize=(8, 6))
# sns.heatmap(corr, mask=mask, cmap='Greys', annot=True, fmt='.2f')
# plt.show()

# Standard Scaler 불러오기 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# # 원본 데이터에 영향을 주지 않기 위해 복사 
data = user_data.copy()

# CustomerID를 제외한 데이터에 스케일링 적용
columns_list = data.iloc[:, 1:].columns # iloc: 데이터 특정 값 추출, columns: 데이터프레임의 열 이름 조회 
data[columns_list] = scaler.fit_transform(data[columns_list])

data.head()


# PCA 불러오기  
from sklearn.decomposition import PCA

# CustomerID를 인덱스로 지정  
data.set_index('CustomerID', inplace=True)

# PCA 적용
pca = PCA().fit(data)


# # Explained Variance의 누적합 계산  
# explained_variance_ratio = pca.explained_variance_ratio_ # explained_variance_ratio_: Explained Variance 비율을 계산해 주는 함수
# cumulative_explained_variance = np.cumsum(explained_variance_ratio) # cumsum: 각 원소의 누적합을 계산하는 함수

# plt.figure(figsize=(15, 8)) 

# # 각 성분의 설명된 분포에 대한 막대 그래프
# barplot = sns.barplot(x=list(range(1, len(cumulative_explained_variance) + 1)), y=explained_variance_ratio, alpha=0.8)

# # 누적 분포에 대한 선 그래프
# lineplot, = plt.plot(range(0, len(cumulative_explained_variance)), cumulative_explained_variance, marker='*', linestyle='--', linewidth=2)

# # 레이블과 제목 설정
# plt.xlabel('Number of Components', fontsize=14)
# plt.ylabel('Explained Variance', fontsize=14)
# plt.title('Cumulative Variance vs. Number of Components', fontsize=18)

# # 눈금 및 범례 사용자 정의
# plt.xticks(range(0, len(cumulative_explained_variance)))
# plt.legend(handles=[barplot.patches[0], lineplot],
#            labels=['Explained Variance', 'Cumulative Explained Variance'])  

# # 두 그래프의 분산 값 표시
# x_offset = -0.3
# y_offset = 0.01
# for i, (ev_ratio, cum_ev_ratio) in enumerate(zip(explained_variance_ratio, cumulative_explained_variance)):
#     plt.text(i, ev_ratio, f"{ev_ratio:.2f}", ha="center", va="bottom", fontsize=10)
#     if i > 0:
#         plt.text(i + x_offset, cum_ev_ratio + y_offset, f"{cum_ev_ratio:.2f}", ha="center", va="bottom", fontsize=10)

# plt.grid(axis='both')   
# plt.show()

# 6개의 주성분을 유지하는 PCA 선언 
pca = PCA(n_components=6)

# 기존 data를 pca에 fit_transform
data_pca = pca.fit_transform(data)

# 압축된 데이터 셋 생성
data_pca = pd.DataFrame(data_pca, columns=['PC'+str(i+1) for i in range(pca.n_components_)])

# 인덱스로 빼 두었던 CustomerID 다시 추가
data_pca.index = data.index
print(data_pca.head())

from sklearn.cluster import KMeans
from collections import Counter

# k=3개의 클러스터로 K-Means 클러스터링 적용
kmeans = KMeans(n_clusters=3, init='k-means++', n_init=10, max_iter=100, random_state=0)
kmeans.fit(data_pca)

# 각 클러스터의 빈도수 구하기
cluster_frequencies = Counter(kmeans.labels_) 

# 빈도수에 기반하여 이전 레이블에서 새 레이블로의 매핑 생성
label_mapping = {label: new_label for new_label, (label, _) in 
                 enumerate(cluster_frequencies.most_common())}

# 매핑을 적용하여 새 레이블 얻기
new_labels = np.array([label_mapping[label] for label in kmeans.labels_])

# 원래 데이터셋에 새 클러스터 레이블 추가
user_data['cluster'] = new_labels

# PCA 버전의 데이터셋에 새 클러스터 레이블 추가
data_pca['cluster'] = new_labels












