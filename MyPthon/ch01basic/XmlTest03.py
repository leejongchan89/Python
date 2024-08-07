from xml.etree.ElementTree import parse

tree = parse(source='Car_info.xml')

myroot = tree.getroot()
print(type(myroot))
print(myroot)

carList = myroot.findall('car') # .findall 반환타입은 list이다.
print(type(carList))
print('총 car 수 : %d' % len(carList))

for currCar in carList: # currCar = <car>
    print('car 구성 정보')
    brand = currCar[0].text # 제로베이스 0부터 시작
    brandName = currCar[0].attrib['name'] # 속성값 가져오기
    model = currCar[1].text
    year = currCar[2].text
    color = currCar[3].text

    print('브랜드 : %s' % (brand))
    print('브랜드 이름 : %s' % (brandName))
    print('모델 : %s' % (model))
    print('제작 년도 : %s' % (year))
    print('색상 : %s' % (color))


    print('-'*30)

#end for