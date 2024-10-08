from xml.etree.ElementTree import Element, ElementTree, SubElement

mydict = {
    'hong':('홍길동', 60, 80, 70),
    'park':('박영희', 50, 70, 95)
}
print(mydict)

# Element etree를 자주 쓴다.
xmlData = Element('students') # 루트 엘리먼트

for key, mytuple in mydict.items(): # .items()는 key, value 둘다 출력해준다.
    # print(key)
    # print(mytuple)
    saram = SubElement(xmlData, 'student') # tag: 자식 엘리먼트
    saram.attrib['id'] = key   # .attrib 속성값 넣기

    kor = mytuple[1]
    eng = mytuple[2]
    math = mytuple[3]

    total = kor + eng + math
    average = total / len(mytuple[1:4]) # 3과 같다.

    saram.attrib['총점'] = str(total)
    saram.attrib['평균'] = '%.3f' % average


    SubElement(saram, '이름').text = mytuple[0]
    SubElement(saram, '국어').text = str(kor)
    SubElement(saram, '영어').text = str(eng)
    SubElement(saram, '수학').text = str(math)



# end for

# 들여쓰기 def
def indent(elem, level=0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
# end def

indent(xmlData)

xmlFile = 'xmlTest_02.xml'
ElementTree(xmlData).write(xmlFile, encoding='UTF-8') # ElementTree import
print(xmlFile + ' 파일이 생성되었습니다.')