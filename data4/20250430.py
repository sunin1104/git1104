import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import kagglehub
import os
import pandas as pd
# //비율 차이 검정
from statsmodels.stats.proportion import proportions_ztest

# // 문제 1
# - 빵집에서는 매일 아침에 구워지는 식빵 한 개의 평균 무게가 500g이 되도록 맞추고자 합니다. 
# 빵집 주인은 오늘 아침에 구운 식빵 중에서 랜덤하게 25개의 식빵을 샘플링하여 무게를 측정했습니다. 
# 그 결과, 표본 평균은 495g, 표준편차는 10g으로 나왔습니다. 
# 빵집 주인이 목표한 500g의 무게를 충족하고 있는지(다시말해 목표 무게를 넘는지 안 넘는지)  5% 유의수준에서 검정해보세요

# // 귀립가설 >> 평균 무게는 500이다
# // 대립가설 >> 평균 무게가 500이 아니다.

# sample_mean=495
# sample_std=10
# alpha=0.05
# s=25
# m0=500

# # // t-값 계산
# t_stat=(sample_mean-m0)/(sample_std/np.sqrt(s))

# df=s-1

# # // 양측검정 p-value 계산
# p_value=2*stats.t.sf(np.abs(t_stat),df)

# if p_value < alpha:
#     print(f" t-값: {t_stat:.4f}, p-value: {p_value:.4f}.\n 유의수준 {alpha}에서 귀무가설을 기각합니다. 빵의 평균 무게는 목표와 다릅니다.")
# else:
#     print(f" t-값: {t_stat:.4f}, p-value: {p_value:.4f}.\n 유의수준 {alpha}에서 귀무가설을 채택합니다. 빵의 평균 무게는 목표와 통게적으로 차이가 없습니다. ")


# // 문제 2
# 문제 1번을 바탕으로 분포를 그리고 t통계량을 빨간색 점선으로, 초록색 점선으로 임계값을 기각역을 초록색으로 칠해보세요.

# x=np.linspace(4,-4,1000)
# y=stats.t.pdf(x,df)

# # // 임계값 구하기
# c_value=stats.t.ppf(1-alpha/2, df)

# plt.figure(figsize=(12,6))
# plt.plot(x,y,color='blue')

# # // t-통계량을 빨간색 점선으로
# plt.axvline(t_stat,color='red',linestyle='--')

# # // 임계값을 초록색 점선으로
# plt.axvline(c_value,color='green',linestyle='--')
# plt.axvline(-c_value,color='green',linestyle='--')

# # // 기각역을 초록색으로
# plt.fill_between(x,y, where=(np.abs(x)>=c_value),color='green')

# plt.title("t-distribution")
# plt.show()


# // 문제 3
# - 어느 학교에서 새로운 교육 프로그램을 도입한 후 학생들의 수학 성적이 향상되었는지 확인하려고 합니다. 
# 프로그램 도입 후 무작위로 선택한 16명의 학생들의 수학 성적 평균은 78점이고, 모집단의 평균은 75점입니다. 
# 모집단의 표준편차는 알 수 없다고 합니다.
# - 유의수준 0.05에서 이 교육 프로그램이 성적 향상에 효과가 있는지 단일 표본 t-검정을 실시하세요.

# sample_scores = [79, 77, 80, 76, 78, 81, 75, 79, 77, 80, 78, 76, 82, 77, 79, 78]

# m03=75
# alpha3=0.05

# s3=len(sample_scores)
# sample_mean3=np.mean(sample_scores)
# sample_std3=np.std(sample_scores)
# df3=s3-1

# # // t-값 계산
# t_stat3=(sample_mean3-m03)/(sample_std3/np.sqrt(s3))

# # // 단측검정 계산
# p_value3=stats.t.sf(t_stat3,df3)

# if p_value3 < alpha3:
#     print(f" t-값: {t_stat3:.4f}, p-value: {p_value3:.4f}.\n 유의수준 {alpha3}에서 귀무가설 기각합니다. 교육프로그램은 효과가 있습니다.")
# else:
#     print(f" t-값: {t_stat3:.4f}, p-value: {p_value3:.4f}.\n 유의수준 {alpha3}에서 귀무가설 채택합니다. 교육프로그램은 효과가 없습니다.")


# // 문제 4
# - 한 연구소에서 두 가지 새로운 다이어트 프로그램의 효과를 비교하려고 합니다. 
# 연구소는 두 그룹의 참가자들을 대상으로 12주간 다이어트 프로그램을 진행한 후 체중 감소량을 측정했습니다.
# - 유의수준 5% 에서 두 그룹 간 평균 체중 감소량에 유의미한 차이가 있는지 독립 표본 t-검정을 실시하세요.

# 그룹 A와 B의 체중 감소량 데이터
# group_A = [5.1, 4.7, 6.2, 4.9, 5.3, 6.1, 5.0, 5.8, 4.8, 5.2]
# group_B = [4.3, 4.1, 3.8, 4.6, 4.0, 4.5, 3.7, 4.2, 3.9, 4.4, 3.5, 4.3]

# alpha4=0.05

# # // 독립 표본 t-검정
# t_stat4,p_value4=stats.ttest_ind(group_A,group_B,equal_var=False)

# if p_value4 < alpha4:
#     print(f" t-값: {t_stat4:.4f}, p-value: {p_value4:.4f}.\n 유의수준 {alpha4}에서 귀무가설을 기각합니다. 다이어트 프로그램은 효과가 있습니다.")
# else:
#     print(f" t-값: {t_stat4:.4f}, p-value: {p_value4:.4f}.\n 유의수준 {alpha4}에서 귀무가설을 채택합니다. 다이어트 프로그램은 효과가 없없습니다.")    


# // 문제 5
# - 운동 프로그램 전후의 체중 변화를 분석하기 위해 10명의 참가자의 체중을 측정했습니다. 
# 유의수준 5%에서 운동 프로그램이 체중 감소에 효과가 있는지 **대응 표본 t-검정**을 실시하세요.
# - 또한, 대응표본t검정에서 등분산 검정이 필요한지 고민해봅시다.

# 운동 전후 체중 데이터
# before = np.array([70, 80, 65, 90, 75, 85, 78, 82, 68, 73])
# after = np.array([68, 78, 64, 88, 74, 83, 77, 80, 67, 72])

# alpha5=0.05

# # // 대응 표본 t-검정
# t_stat5,p_value5=stats.ttest_rel(before,after)

# if p_value5 < alpha5:
#     print(f" t-값: {t_stat5:.4f}, p-value: {p_value5:.4f}.\n 유의수준 {alpha5}에서 귀무가설을 기각합니다. 고혈압약은 효과가 있습니다.")
# else:
#     print(f" t-값: {t_stat5:.4f}, p-value: {p_value5:.4f}.\n 유의수준 {alpha5}에서 귀무가설을 채택합니다. 고혈압약은 효과가 없습니다.")


# // 문제 6
# - Quest 05-01의  Online Retail II 데이터에서 표본을 추출하여 모집단의 평균을 추정해보세요.
# - 영국(United Kingdom)에서 주문된 데이터 에서 30개, 100개, 300개의 샘플을 무작위 추출하여 평균 구매 금액(Total Price)를 계산해보세요. 
# 표본의 크기가 커질 수록 모집단의 평균과 가까워지는지 확인해보세요.

# Download latest version
# path = kagglehub.dataset_download("mashlyn/online-retail-ii-uci")
# print("Path to dataset files:", path)
# retail = pd.read_csv(path + '/' + os.listdir(path)[0])
# # print(retail.head(3))

# uk=retail[retail['Country']=='United Kingdom']

# uk['Total Price'] = pd.to_numeric(uk['Quantity'], errors='coerce') * pd.to_numeric(uk['Price'], errors='coerce')
# uk = uk[uk['Total Price'].notnull() & (uk['Total Price'] > 0)]

# for size in [30,100,300]:
#     sample=uk.sample(n=size, random_state=42)
#     mean_price=sample['Total Price'].mean()
#     print(f"Sample size: {size}, Mean TotalPrice: {mean_price:.2f}")


# // 문제 7
# 영국 데이터에서 TotalPrice를 사용하여 95% 신뢰 구간을 계산하세요. 
# 또한 표본의 크기가 30,100, 300으로 변하면서 신뢰구간이 변하는 형태를 확인해 보세요.

# 신뢰 구간 계산 함수
# def confidence_interval(data, confidence=0.95):
#     mean = data.mean()
#     std_err = stats.sem(data)
#     interval = stats.t.interval(confidence, len(data)-1, loc=mean, scale=std_err)
#     return mean, interval

# # 샘플 크기에 따른 신뢰 구간 비교
# sample_sizes = [30, 100, 300]
# for size in sample_sizes:
#     sample = uk.sample(size, random_state=42)
#     mean, interval = confidence_interval(sample)
#     print(f"Sample size: {size}, Mean: {mean:.2f}, 95% CI: {interval}")


# // 문제 8
# - 영국과 독일의 고객의 평균 구매금액(Total Price)가 동일한지 검정해보세요. 
# 귀무가설과 대립가설을 세우고 통계검정을 통해 결과를 해석하세요
# - 영국과 독일의 분포는 등분산성은 따른다고 가정

# // 귀무가설 >> 영국과 독일 평균 구매금액은 동일하다.
# // 대립가설 >> 영국과 독일 평균 구매금액은 동일하지 않다.

# germany=retail[retail['Country']=='germany']
# germany['Total Price']=pd.to_numeric(germany['Quantity'], errors='coerce')*pd.to_numeric(germany['Price'], errors='coerce')

# germany=germany[(germany['Total Price'].notnull())&(germany['Total Price']>0)]

# # // 등분산성 따르고, 통계 검정
# t_stat8,p_value8=stats.ttest_ind(uk['Total Price'],germany['Total Price'],equal_var=True)

# alpha8=0.05

# if p_value8 >= alpha8:
#     print(" 귀무가설 기각.\n 영국과 독일 고객의 평균 구매 금액에 유익한 차이가 있습니다.")
# else:
#     print(" 귀무가설 채택.\n 영국과 독일 고객의 평균 구매 금액에 유익한 차이가 없습니다.")


# // 문제 9
# A/B test스타트업A에서 새로운 여행 패키지 상품 판매를 진행하고자 합니다. 
# 패키지 판매 기획자는 새로운 패키지의 상품 판매 효율을 높이고 싶어하며, 
# 이를 위해 기존에 상품이 판매되던 웹 페이지 (페이지 A) 가 아닌 새로운 웹 페이지 (페이지 B)를 통해 판매하고자 합니다. 
# 패키지 판매 기획자는 신규 웹페이지 (페이지 B) 가 기존 (페이지 A) 대비 효과가 좋은 지 확인하기 위해 A/B 테스트를 진행하였습니다.

# 귀무가설 >> 페이지a와 페이지b의 효과가 동일하다.
# 대립가설 >> 페이지a와 페이지b의 효과가 다르다.

page_a=1000
page_buyA=80

page_b=200
page_buyB=22

a_b_cnt=[page_buyA,page_buyB]
a_b=[page_a,page_b]

z_stat9,p_value9=proportions_ztest(a_b_cnt,a_b)

alpha9=0.05

if p_value9 < alpha9:
    print(f" z_stat: {z_stat9:.2f}, p-value: {p_value9:.2f}.\n 귀무가설 기각. 두 페이지의 비율에 차이가 있다.")
else:
    print(f" z_stat: {z_stat9:.2f}, p-value: {p_value9:.2f}.\n 귀무가설 채택. 두 페이지의 비율에 차이가 없다.")

# 결과를 바탕으로 패키지 기획자는 페이지 B의 효과에 대해 어떤 결정을 해야 할지 서술해 주세요. 
'''
>>> 페이지 B가 기존 페이지 A보다 통계적으로 유의미하다고 볼 수 없습니다.
페이지 B를 도입하는 것보다 디자인을 개선하거나 페이지 내용을을 수정하고 다시 재테스트하는 것이 좋아보입니다.

'''

# // 문제 10
# A/B 테스트의 결과가 통계적으로 유의하나 효과의 차이 자체는 매우 작은 경우, 
# 어떤 의사결정을 할 수 있을지 사례를 통해 설명해 주세요.
'''
사례: 전자상거래 사이트의 제품 추천 기능 개선

<상황>
페이지 A는 기존의 제품 추천 시스템이 적용된 웹 페이지입니다.

페이지 B는 새로운 제품 추천 알고리즘을 적용한 웹 페이지입니다.

두 페이지에 대한 A/B 테스트 결과는 다음과 같습니다:

페이지 A (기존 시스템): 구매 전환율 2.1%

페이지 B (새 시스템): 구매 전환율 2.2%

<결과 분석>
통계적 검정 결과:

p-value는 0.01로 통계적으로 유의미한 차이가 있음을 보여줍니다.

z-stat는 약간 높은 값으로, 두 페이지의 차이가 우연에 의한 것이 아닐 확률이 높다고 할 수 있습니다.

효과 크기:

페이지 B의 전환율이 2.1%에서 2.2%로 0.1% 증가한 것입니다. 이는 매우 작은 차이입니다.

A/B 테스트에서 통계적으로 유의미한 차이가 나더라도, 효과 크기가 매우 작은 경우, 
실제 비즈니스 결정을 내릴 때는 그 효과의 실질적인 영향을 반드시 고려해야 하며, 
비용 대비 효율성을 잘 평가하고 장기적인 전략적 목표를 우선시해야 합니다.
'''

# // 회고
# 이번에 통계 검정에 대해 다룬 내용을 통해 독립 표본 검정, 단측 검정, 단일 표본 검정, 대응 표본 검정, 비율 검정에 대해 손에 익히고, 
# 헷갈렸던 부분들을 정리하는 시간이었습니다. 각 검정 방법에 대해 조금 더 명확히 이해할 수 있게 되었고, 
# 앞으로 데이터 분석에서 이러한 방법들을 어떻게 활용할지에 대해 고민해볼 수 있었습니다.




