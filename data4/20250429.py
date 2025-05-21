import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = r"C:\Users\USER\Downloads\online+retail+ii\online_retail_II.xlsx"

# df= pd.read_excel(path)

# // 시트 이름 확인
# excel_file = pd.ExcelFile(path)
# print(excel_file.sheet_names)

# Columns =
# - `Invoice`: Invoice number. Nominal. A 6-digit integral number uniquely assigned to each transaction. If this code starts with the letter 'c', it indicates a cancellation.
# - `StockCode`: Product (item) code. Nominal. A 5-digit integral number uniquely assigned to each distinct product.
# - `Description`: Product (item) name. Nominal.
# - `Quantity`: The quantities of each product (item) per transaction. Numeric.
# - `InvoiceDate`: Invice date and time. Numeric. The day and time when a transaction was generated.
# - `Price`: Unit price. Numeric. Product price per unit in sterling (Â£).
# - `CustomerID`: Customer number. Nominal. A 5-digit integral number uniquely assigned to each customer.
# - `Country`: Country name. Nominal. The name of the country where a customer resides.

df1 = pd.read_excel(path, sheet_name='Year 2009-2010')
df2 = pd.read_excel(path, sheet_name='Year 2010-2011')
df = pd.concat([df1, df2], ignore_index=True)

# // 문제 1
print(df.head())


# // 문제 2
df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])
df=df.dropna(subset=['Customer ID'])
print(df.head())

# Customer ID를 정수형으로 변환한 후, InvoiceDate를 기준으로 데이터를 정렬하세요.
df['Customer ID']=df['Customer ID'].astype('Int64')
df=df.sort_values(by='InvoiceDate')
print(df.head())

# 금액을 나타내는 새로운 컬럼 Total 을 생성하세요 (Quantity와 Price를 곱한 값).
df['Total']=df['Quantity']*df['Price']
print(df['Total'])


# // 문제 3
# Country 컬럼을 기준으로 Customer ID의 유니크한 값을 계산하여 나라별 구매 고객 수를 시각화 해보세요
country_customer=df.groupby('Country')['Customer ID'].nunique()

# plt.figure(figsize=(12,6))
# country_customer.plot(kind='bar',color='purple')
# plt.title('Countries with Largest Number of Unique Customers')
# plt.ylabel('Number of Unique Customers')
# plt.xlabel('Year-Month')
# plt.show()


# // 문제 4
# 신규 고객 분석을 위해 고객의 첫 구매 시점을 기준으로 월별 신규 유입 고객 수를 계산하세요.
# // 고객의 첫 구매 시점
first_buy=df.groupby('Customer ID')['InvoiceDate'].min()

# // 월별로 보고 싶음
first_buy_M=first_buy.dt.to_period('M')

# // 신규 유입 고객 수 계산
first_M_cnt=first_buy_M.value_counts().sort_index()

print(first_M_cnt)

# // 각 고객의 첫 구매 날짜를 추출하고, 월별 신규 고객 수를 시각화하세요.
# plt.figure(figsize=(12,6))
# first_M_cnt.plot(kind='bar',color='blue',alpha=0.4)
# plt.title('Monthly New Customers')
# plt.xlabel('Year-Month')
# plt.ylabel('Number of New Customers')
# plt.show()


# // 문제 5
# 모든 고객 중 첫 구매 이후 총 구매 금액이 특정 기준 금액 (£50) 이상인 고객을 활성화된 고객으로 정의합니다.
my_customer=df[df['InvoiceDate']>df['Customer ID'].map(first_buy)]

tot_my_customer=my_customer.groupby('Customer ID')['Total'].sum()

tot50=tot_my_customer[tot_my_customer>=50]
print(tot50)

# 전체 고객 수와 활성화된 고객 수를 비교하여 활성화율을 도출하세요.
tot50_cnt=tot50.count()

tot_all=df['Customer ID'].nunique()

my_customer_rate=(tot50_cnt/tot_all)*100

print(f"총 고객 수: {tot_all}")
print(f"활성화된 고객 수 (첫 구매 후 50이상 지출한 고객): {tot50_cnt}")
print(f"고객 활성화율: {my_customer_rate:.2f}%")


# // 문제 6
# 분기별 활성 사용자(MAU)를 분석하여 고객 유지 현황을 파악하세요.
# // 분기 추출
df['Quarter']= df['InvoiceDate'].dt.to_period('Q')

# // 분기별 활성 사용자 수
quantity_customer=df.groupby('Quarter')['Customer ID'].nunique()

# plt.figure(figsize=(12,6))
# quantity_customer.plot(kind='bar')
# plt.title('분기별 활성 사용자')
# plt.show()

# // 분기별 활성 고객 데이터로 pivot-table 생성
# print(df.columns)

retention= pd.pivot_table(df, 
                          values='Invoice',
                          index='Customer ID',
                          columns='Quarter',
                          aggfunc='count')
print(retention.head())

retention=retention.notnull().astype(int)

# 분기별 활성 고객 수를 계산하고, 이를 시각화하여 고객 유지 트렌드를 분석하세요.
#히트맵 코드
# heatmap = sns.heatmap(
#     data=retention,
#     annot=True,
#     fmt='.2f',
#     cmap='Greens',
#     cbar_kws={'label':'Retention Rate,%'},
#     linewidths=0.5,
#     linecolor='gray',
#     vmin=0, vmax=100
# )
# plt.show()


# // 문제 7
# 분기단위의 활성 사용자의 평균 구매수량을 분석하세요.
heatmap = sns.heatmap(
    data=average_quantity,
    annot=True,                # 셀 내부에 값 표시
    fmt='.1f',                 # 텍스트 형식 (소수점 1자리)
    cmap='Blues',              # 색상 팔레트
    cbar_kws={'label': 'Average Quantity'},  # 컬러바 제목
    linewidths=0.5,            # 셀 간격
    linecolor='gray',          # 셀 경계 색상
    vmin=0                     # 최소값 설정 (필요 시 조정 가능)
)



# // 문제 8

# // 문제 9






# import numpy as np

# // 문제 10
# 어떤 회사의 고객 대기시간은 5분에서 15분 사이의 균등분포를 따릅니다. 
# 고객 100명이 대기한 시간을 시뮬레이션하고, 평균 대기시간과 표준편차를 계산하세요.
# np.random.seed(42)

# wait_times=np.random.uniform(low=5, high=15, size=100)

# mean_wait=np.mean(wait_times)

# std_wait=np.std(wait_times)

# print(f"평균 대기시간:{mean_wait:.2f}")
# print(f"표준편차:{std_wait:.2f}")


# // 문제 11 - 이항분포 binomial
# 한 신제품의 초기 성공 확률이 0.3이라고 가정합니다. 
# 10회의 시뮬레이션에서 성공한 횟수를 구하고, 각 성공 여부를 출력하세요.
# np.random.seed(42)

# n=1
# p=0.3

# sucesses=np.random.binomial(n,p,size=10)

# # // 성공 횟수 구하기
# ss=np.sum(sucesses)

# print(f"각 시도 결과: {sucesses}")
# print(f"성공 횟수: {ss}")


# // 문제 12
# 한 수업에서 학생 20명이 5문제로 구성된 퀴즈를 치릅니다. 각 문제의 정답 확률은 0.7이라고 가정할 때, 
# 각 학생이 맞힌 점수를 시뮬레이션하고, 전체 학생의 평균 점수를 계산하세요.
# np.random.seed(42)

# n=5
# p=0.7

# check=np.random.binomial(n,p,size=20)

# # // mean
# avg_stu=np.mean(check)

# print(f"학생별 점수: {check}")
# print(f"평균 점수: {avg_stu:.2f}")


# // 문제 13 정규분포 - normal(loc=,scale=,size=)
# 한 공장에서 생산되는 제품의 무게는 평균 50g, 표준편차 5g의 정규분포를 따릅니다.1000개의 제품 무게를 시뮬레이션하고, 
# 무게가 45g 이상 55g 이하인 제품의 비율을 계산(변수명: within_range)하세요. 
# 무게 분포의 히스토그램을 그리세요. 
# from scipy.stats import norm

# np.random.seed(42)

# product_weight=np.random.normal(loc=50,scale=5,size=1000)

# # // 비율계산
# within_range=np.mean((product_weight>=45)&(product_weight<=55))

# print(f"45g 이상 55g 이하 비율: {within_range:.2%}")

# # // 무게 분포 히스토그램 그리기
# plt.hist(product_weight, bins='auto', color='skyblue',alpha=0.8,density=True)

# x = np.linspace(min(product_weight), max(product_weight), 1000)
# y= norm.pdf(x, loc=50,scale=5)

# plt.plot(x, y, color='red')
# plt.title("Product Weight Distribution")
# plt.xlabel("Weight (g)")
# plt.ylabel("Density")
# plt.show()


# //회고 
# 이번 분석 과정에서 시각화 방법을 어느 정도 손에 익힌 것 같습니다. 
# 다양한 데이터를 시각적으로 표현하면서 데이터를 어떻게 더 직관적으로 전달할 수 있는지에 대한 감각을 키운 것 같습니다.
# 예를 들어, 히트맵, 막대 그래프, 시간대별 시각화 등을 활용하며 데이터를 시각적으로 이해하는 데 도움이 많이 되었습니다.

# 마지막에는 난수 생성을 통해 실제 상황을 시뮬레이션하는 연습을 했습니다. 
# 이를 통해 균등분포, 이항분포, 정규분포에 대한 시뮬레이션을 진행하고, 각 분포에 따른 평균과 표준편차를 계산하는 방법을 익혔습니다.