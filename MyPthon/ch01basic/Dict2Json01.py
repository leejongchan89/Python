# 중첩된 dict 형태
# dict -> str -> list
humanDict = {
    'age':20, 'name':'유현식', 'hobby':'독서',
    'address':{'city':'seoul', 'gu':'마포구', 'zipcode':'12345'}
}
print(type(humanDict))
print(humanDict)

# .dumps dict형식을 str형식으로 변환

# ensure_ascii=False 한글 그대로 보이게
# indent=4 세로로 보기
# sort_keys=True abc순으로 정렬
import json
humanString = json.dumps(humanDict, ensure_ascii=False, indent=4, sort_keys=True)
print(type(humanString))
print(humanString)

humanJson = json.loads(humanString) # .loads()는 String을 List 타입으로 바꿔준다.
print('이름 : %s' % humanJson['name'])
print('취미 : %s' % humanJson['hobby'])
print('나이 : %s' % humanJson['age'])
print('시도 : %s' % humanJson['address']['city'])
print('군구 : %s' % humanJson['address']['gu'])
print('우편 번호 : %s' % humanJson['address']['zipcode'])