import pandas as pd
myencoding = 'UTF-8'
filename = './../data/kmdb_get_movie_list_100.csv' # . 은 현위치 .. 은 상위 폴더
dataframe = pd.read_csv(filename, encoding=myencoding)
# print(dataframe.info())

print('행 색인 정보 확인')
print(dataframe.index)

print('열 색인 정보 확인')
print(dataframe.columns)

print('컬럼별 데이터 유형 확인')
print(dataframe.dtypes)

# 범주형 데이터와 연속형 데이터를 한 눈에 체크하려고
for column in dataframe.columns:
    print(column)
    # print(dataframe[column].unique())
    # print('-'*30)

# sorted 함수는 오름차순으로 정렬해주는 내장 함수입니다.
# print(sorted(dataframe['movieCd'].unique()))

print('숫자 형식만 필터링하기')
print('before count : ' + str(len(dataframe)))
dataframe = dataframe[dataframe['movieCd'].str.isdigit()] # .str.isdigit() 오직 숫자로된 거만 필터링
print('after count : ' + str(len(dataframe)))

print(dataframe['repGenreNm'].unique())

print('결측치 필터링하기')
print('before count : ' + str(len(dataframe)))
dataframe = dataframe[dataframe['repGenreNm'].notna()] # .notna() na값이 아닌 것들만 필터링
print('after count : ' + str(len(dataframe)))

# 'movieCd' 열을 숫자형 형식으로 변환
dataframe['movieCd'] = pd.to_numeric(dataframe['movieCd'])

print('컬럼별 데이터 유형 확인')
print(dataframe.dtypes)

# 제작년도(prdtYear) 컬럼만 추출하기
prdtYear = dataframe['prdtYear']
print(type(prdtYear))

# 구조 분석
print('시리즈 요소 개수 확인 : ' + str(prdtYear.size))
print('형상 확인 : ' + str(prdtYear.shape))
print('len(prdtYear) : ' + str(len(prdtYear)))
print('count() : ' + str(prdtYear.count())) # 결측치는 카운팅 하지 않는다.
print('타입 확인 : ' + str(prdtYear.dtype))
print('누락된 데이터 있나요? : ' + str(prdtYear.hasnans))
print('모든 항목이 unique한가요? : ' + str(prdtYear.is_unique))

# 칼럼 변수들을 그룹핑해서 카운팅
print(prdtYear.value_counts())

filename = './../data/kmdb_get_movie_list_100_new.csv' # . 은 현위치 .. 은 상위 폴더
dataframe.to_csv(filename, index=False, encoding='UTF-8')
print(filename + ' 파일이 저장되었습니다.')